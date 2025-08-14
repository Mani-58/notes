from pydantic import BaseModel, EmailStr
from typing import List

class NoteBase(BaseModel):
    title: str
    content: str

class NoteCreate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: str
    owner_id: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: str
    email: EmailStr
    notes: List[str] = []