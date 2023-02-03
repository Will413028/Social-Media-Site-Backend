from fastapi import HTTPException, status
from schemas.post import PostBase
from database.models import Post
from sqlalchemy.orm.session import Session
from datetime import datetime


def get_all_posts(db: Session):
    posts = db.query(Post).all()

    return posts 


def get_post(db: Session, id: int):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f'Post with id {id} not found')

    return post


def create_post(db: Session, request: PostBase):
    new_post = Post(
        image_url = request.image_url,
        image_url_type = request.image_url_type,
        caption = request.caption,
        timestamp = datetime.now(),
        user_id = request.user_id
    )
    try:
        db.add(new_post)
        db.commit()
        db.refresh(new_post)
        return new_post
    except Exception as e:
        db.rollback()
        raise Exception(str(e))
