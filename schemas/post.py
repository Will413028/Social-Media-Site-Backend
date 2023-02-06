from pydantic import BaseModel
from datetime import datetime
from schemas.user import User
from schemas.comment import Comment

class PostBase(BaseModel):
    image_url: str
    image_url_type : str
    caption: str
    user_id: int

class PostDisplay(BaseModel):
    id: int
    image_url: str
    image_url_type: str
    caption: str
    timestamp: datetime
    user: User
    comments: list[Comment]
    class Config():
        orm_mode = True