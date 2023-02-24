from pydantic import BaseModel
from datetime import datetime
from schemas.user import User


class Comment(BaseModel):
    text: str
    timestamp: datetime
    user: User

    class Config():
        orm_mode = True


class CommentBase(BaseModel):
    text: str
    timestamp: datetime
