from fastapi import HTTPException, status
from schemas.comment import CommentBase
from database.models import Post, User, Comment
from sqlalchemy.orm.session import Session
from datetime import datetime


def get_all_comments(db: Session, post_id: int):
    comments = db.query(Comment).filter(Comment.post_id==post_id).all()
    return comments
    

def get_comment(db: Session, id: int):
    comment = db.query(Comment).filter(Comment.id == id).first()

    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'Comment with id {id} not found')

    return comment


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
