from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import user, post, comment, authentication


app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(authentication.router)

app.mount("/images", StaticFiles(directory="images"), name="images")