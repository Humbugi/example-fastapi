from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import post, user, auth, vote

# tells sqlalchemy to run sql statements to create tables (not needed if alembic in use)
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/")
async def root():
    return {"message": "Welcome to my api"}
