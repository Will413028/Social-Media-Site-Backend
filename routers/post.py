from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.post import PostBase, PostDisplay
from database.base import get_db_session
from core import post

router = APIRouter(
    prefix='/posts',
    tags=['post']
)

image_url_types = ['absolute', 'relative']


@router.get('/', response_model=list[PostDisplay])
def get_posts(db: Session = Depends(get_db_session)):
    return post.get_all_posts(db)


@router.get('/{id}', response_model=PostDisplay)
def get_post(id: int, db: Session = Depends(get_db_session)):
    return post.get_post(db, id)


@router.post('', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db_session)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='image_url_type must be absolute or relative')
    try:
        return post.create_post(db, request)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))