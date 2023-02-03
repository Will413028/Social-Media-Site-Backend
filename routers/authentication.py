from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session
from database.base import get_db_session
from database.models import User
from utils.hash import Hash
from utils import oauth2


router = APIRouter(
  tags=['authentication']
)

@router.post('/login')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db_session)):
  user = db.query(User).filter(User.username == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
  if not Hash.verify(user.password, request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")
  
  access_token = oauth2.create_access_token(data={'username': user.username})

  return {
    'access_token': access_token,
    'token_type': 'bearer',
    'user_id': user.id,
    'username': user.username
  }