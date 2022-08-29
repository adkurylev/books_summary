from datetime import datetime
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    email: str
    timestamp: Optional[datetime] = None

class Book(BaseModel):
    id: Optional[UUID] = uuid4()
    title: str
    content: str
    summary: Optional[str]

class Like(BaseModel):
    id: Optional[UUID] = uuid4()
    user_id: UUID
    book_id: UUID