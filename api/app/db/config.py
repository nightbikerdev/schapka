from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


SQLALCHEMY_DATABASE_URL = "postgresql://michael:scott@localhost/db"

# Create a database engine
async_engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL, 
    future=True, 
    echo=False
)

# Create a session factory
async_session = sessionmaker(
    bind=async_engine, 
    autocommit=False,
    autoflush=False,
    expire_on_commit=False, 
    class_=AsyncSession,
)

# Define a base class for declarative ORM models
Base = declarative_base()
