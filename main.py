from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import user, post

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)

app.mount("/images", StaticFiles(directory="images"), name="images")