from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.comment import CommentBase, Comment
from schemas.user import UserBase
from database.base import get_db_session
from core import comment
from utils.oauth2 import get_current_user

router = APIRouter(
    prefix='/posts',
    tags=['comment']
)


@router.post('/{post_id}/comment', response_model=Comment)
def create_comment(post_id: int, request: CommentBase, db: Session = Depends(get_db_session), current_user: UserBase = Depends(get_current_user)):
    user_id = current_user.id
    try:
        return comment.create_comment(db, request, post_id, user_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))