from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.auth import router as auth_router, SECRET_KEY, ALGORITHM
from app.database import connect_to_mongo
from app.crud import create_note, get_user_notes
from app.schemas import NoteCreate
from jose import jwt, JWTError

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.on_event("startup")
async def startup():
    await connect_to_mongo()

app.include_router(auth_router)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/notes")
async def create_user_note(note: NoteCreate, user_id: str = Depends(get_current_user)):
    return await create_note(note, user_id)

@app.get("/notes")
async def read_user_notes(user_id: str = Depends(get_current_user)):
    return await get_user_notes(user_id)