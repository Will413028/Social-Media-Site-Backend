from  database.base import Base
from sqlalchemy import Column, Integer, String



class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(36))
    email = Column(String(36))
    password = Column(String(128))
