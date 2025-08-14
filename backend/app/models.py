from beanie import Document, Link
from pydantic import EmailStr
from typing import Optional, List

class User(Document):
    email: EmailStr
    hashed_password: str
    notes: Optional[List[Link["Note"]]] = []

class Note(Document):
    title: str
    content: str
    owner: Link[User]