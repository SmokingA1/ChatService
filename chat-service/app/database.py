from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from typing import AsyncGenerator
import os 

load_dotenv()

DATABASE = os.getenv('DATABASE_URL')

engine = create_async_engine(DATABASE, echo=True)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_ = AsyncSession)

Base = declarative_base()

async def get_db() -> AsyncGenerator[AsyncSession, None, None]:
    async with SessionLocal() as session:
        yield session
        