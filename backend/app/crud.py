from fastapi import HTTPException
from app.models import Note, User
from app.schemas import NoteCreate
from beanie import PydanticObjectId

async def create_note(note_data: NoteCreate, user_id: str):
    user = await User.get(PydanticObjectId(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    note = Note(**note_data.dict(), owner=user)
    await note.insert()
    user.notes.append(note)
    await user.save()
    return note

async def get_user_notes(user_id: str):
    user = await User.get(PydanticObjectId(user_id))
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    notes = await Note.find(Note.owner.id == user.id).to_list()
    return notes