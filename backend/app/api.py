from typing import List
from uuid import UUID
from fastapi import FastAPI, HTTPException
from app.schemas import Book, Like, User
from app.database import *

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "There is nothing here :("}

# USERS

@app.get("/api/v1/users")
async def fetch_users() -> List[User]:
    return users

@app.get("/api/v1/users/{user_id}")
async def fetch_user_by_id(user_id: UUID) -> User:
    for user in users:
        if user_id == user.id:
            return user

    raise HTTPException(
        status_code=404,
        detail=f"User {user_id} not found"
    )

@app.post("/api/v1/users")
async def register_user(user: User) -> UUID:
    users.append(user)
    return {"id": user.id}

# BOOKS

@app.get("/api/v1/books")
async def fetch_books() -> List[Book]:
    pass

@app.put("/api/v1/books/{book_id}")
async def make_summary(book_id: UUID):
    pass

# LIKES

@app.post("/api/v1/likes")
async def add_like(like: Like) -> UUID:
    pass

@app.delete("/api/v1/likes")
async def remove_like(like: Like):
    pass

@app.get("/api/v1/likes/{user_id}")
async def get_likes_by_user(user_id: UUID) -> List[Like]:
    pass