from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models import User, Note

async def connect_to_mongo():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie(database=client.notes_db, document_models=[User, Note])