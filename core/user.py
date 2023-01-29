from schemas.user import UserBase
from database.models import User
from sqlalchemy.orm.session import Session


def create_user(db: Session, request: UserBase):
    new_user = User(
        username = request.username,
        email = request.email,
        password = request.password
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e:
        db.rollback()
        raise Exception(str(e))
    return new_user

