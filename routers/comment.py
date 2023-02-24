from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.comment import CommentBase, Comment
from schemas.user import UserBase
from database.base import get_db_session
from core import comment
from utils.oauth2 import get_current_user


router = APIRouter(
    prefix='/comment',
    tags=['comment']
)


@router.get('/{id}', response_model=Comment)
def get_comment(id: int, db: Session = Depends(get_db_session)):
    return comment.get_comment(db, id)
