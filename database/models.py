from database.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(36))
    email = Column(String(36))
    password = Column(String(128))
    posts = relationship('Post', back_populates='user')
    comments = relationship('Comment', back_populates='user')
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String(255))
    image_url_type = Column(String(36))
    caption = Column(String(36))
    timestamp = Column(DateTime)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates="posts")
    comments = relationship('Comment', back_populates="post")

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String(255))
    timestamp = Column(DateTime)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post', back_populates="comments")
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates="comments")

class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')
    comment_id = Column(Integer, ForeignKey('comment.id'))
    comment = relationship('Comment')
    timestamp = Column(DateTime)

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True, index=True)
    follower_id = Column(Integer, ForeignKey('user.id'))
    follower = relationship('User', backref="follower", uselist=False, foreign_keys=[follower_id])
    followee_id = Column(Integer, ForeignKey('user.id'))
    follower = relationship('User', backref="followee_id", uselist=False, foreign_keys=[followee_id])
class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True, index=True)
    message = Column(String(255))
    sender_id = Column(Integer, ForeignKey('user.id'))
    sender = relationship('User', backref="sender_of_message", uselist=False, foreign_keys=[sender_id])
    receiver_id = Column(Integer, ForeignKey('user.id'))
    receiver = relationship('User', backref="receiver_of_message", uselist=False, foreign_keys=[receiver_id])
    status = Column(Boolean)
    timestamp = Column(DateTime)
