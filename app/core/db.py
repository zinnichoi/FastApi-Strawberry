import sys

from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession

from app import settings

db_connection_str = settings.db_async_connection_str

if "pytest" in sys.modules:
    db_connection_str = settings.db_async_test_connection_str

async_engine = create_async_engine(
    db_connection_str,
    echo=True,
    future=True
)

async_session = sessionmaker(
        bind=async_engine, class_=AsyncSession, expire_on_commit=False
    )