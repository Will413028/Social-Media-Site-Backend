from fastapi import FastAPI
from database import models
from database.base import engine
from routers import user


app = FastAPI()

app.include_router(user.router)

models.Base.metadata.create_all(engine)