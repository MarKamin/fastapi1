from fastapi import FastAPI
from app.modelsfol import models
from app.databfol.database import engine, SessionLocal, get_db
from app.routers import post, user, auth, vote
from app.modelsfol.config import settings
from fastapi.middleware.cors import CORSMiddleware



#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["https://www.google.lt"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# uvicorn app.main:app --reload
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return{"message": "Hell World"}