import os

from app.core.config import DATABASE_URL
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


CONTAINER_DSN: str = os.environ.get('CONTAINER_DSN', '')
DB_URL: str = CONTAINER_DSN if CONTAINER_DSN else DATABASE_URL

engine = create_async_engine(
    DB_URL,
    echo=True,
    future=True,
)


def async_session_generator():
    return sessionmaker(
        engine, class_=AsyncSession
    )