from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL
SQLALCHEMY_DATABASE_URL = "postgresql://michael:scott@localhost/db"

# Create a database engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define a base class for declarative ORM models
Base = declarative_base()

# Function to get the database URL
def get_db_url():
    return SQLALCHEMY_DATABASE_URL