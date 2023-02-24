from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.base import get_db_session
from core import follower
from utils.oauth2 import get_current_user
from schemas.user import UserBase


router = APIRouter(
    prefix='/followers',
    tags=['followers']
)


@router.post('')
def create_follow(followee_id: int, db: Session = Depends(get_db_session), current_user: UserBase = Depends(get_current_user)):
    return follower.create_follow(db, followee_id, current_user.id)


@router.delete('/{followee_id}')
def cancel_follow(followee_id: int, db: Session = Depends(get_db_session), current_user: UserBase = Depends(get_current_user)):
    return follower.cancel_follow(db, followee_id, current_user.id)
