from schemas.user import UserBase
from database.models import User
from sqlalchemy.orm.session import Session
from utils.hash import Hash


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