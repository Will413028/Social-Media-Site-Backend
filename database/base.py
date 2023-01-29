from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
 
engine = create_engine("mysql+mysqlconnector://root:1234@localhost:4000/social-web-db", pool_pre_ping=True, pool_recycle=3600)
 
Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
 
Base = declarative_base()
 
def get_db_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()
