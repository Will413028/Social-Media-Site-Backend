from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
from schemas.post import PostBase, PostDisplay
from schemas.user import UserBase
from database.base import get_db_session
from core import post
import random, string, shutil
from utils.oauth2 import get_current_user

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
def create_post(request: PostBase, db: Session = Depends(get_db_session), current_user: UserBase = Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='image_url_type must be absolute or relative')
    try:
        return post.create_post(db, request)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@router.post('/image')
def upload_image(image: UploadFile = File(...)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters + string.digits) for i in range(6))
    new = f'_{rand_str}.'
    filenamw = new.join(image.filename.rsplit('.', 1))
    path = f'images/{filenamw}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {'filename': path}