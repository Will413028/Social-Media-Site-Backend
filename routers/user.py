from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.user import UserDisplay, UserBase
from database.base import get_db_session
from core import user

router = APIRouter(
    prefix='/users',
    tags=['user']
)


@router.get('/', response_model=list[UserDisplay])
def get_users(db: Session = Depends(get_db_session)):
    return user.get_all_users(db)


@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db_session)):
    return user.get_user(db, id)


@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db_session)):
    try:
        return user.create_user(db, request)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))