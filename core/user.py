from fastapi import HTTPException, status
from schemas.user import UserBase
from database.models import User
from sqlalchemy.orm.session import Session
from utils.hash import Hash


def get_all_users(db: Session):
    users = db.query(User).all()

    return users 


def get_user(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'User with id {id} not found')

    return user


def create_user(db: Session, request: UserBase):
    new_user = User(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except Exception as e:
        db.rollback()
        raise Exception(str(e))

def get_user_by_username(db: Session, username: str):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'User with username {username} not found')
    return user
