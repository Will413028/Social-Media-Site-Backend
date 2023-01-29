from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserDisplay, UserBase
from database.base import get_db_session
from core import user

router = APIRouter(
    prefix='/users',
    tags=['user']
)


@router.post('', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db_session)):
    try:
        return user.create_user(db, request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))