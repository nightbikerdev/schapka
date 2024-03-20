import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.db.config import Base, SQLALCHEMY_DATABASE_URL

@pytest_asyncio.fixture(scope="session")
def engine():
    engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def async_db_session(async_db_engine):
    async_session = sessionmaker(
        bind=async_db_engine,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
        class_=AsyncSession,
    )
    async with async_session() as session:
        yield session