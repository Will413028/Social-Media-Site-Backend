from fastapi import HTTPException, status
from schemas.comment import CommentBase
from database.models import Comment
from sqlalchemy.orm.session import Session
from datetime import datetime


def create_comment(db: Session, request: CommentBase, post_id: int, user_id: int):
    new_comment = Comment(
        text = request.text,
        timestamp = datetime.now(),
        post_id = post_id,
        user_id = user_id
    )
    try:
        db.add(new_comment)
        db.commit()
        db.refresh(new_comment)
        return new_comment
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))