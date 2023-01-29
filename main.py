from fastapi import FastAPI
from database import models
from database.base import engine

app = FastAPI()


@app.get('/')
def hello():
    return {'message': 'Hello world'}

models.Base.metadata.create_all(engine)