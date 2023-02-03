from database.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(36))
    email = Column(String(36))
    password = Column(String(128))
    posts = relationship('Post', back_populates='user')

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(255))
    image_url_type = Column(String(36))
    caption = Column(String(36))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates="posts")