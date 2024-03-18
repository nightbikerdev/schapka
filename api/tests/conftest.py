import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..database import Base, get_db_url

@pytest.fixture(scope="session")
def engine():
    engine = create_engine(get_db_url(), echo=True)
    Base.metadata.create_all(engine)
    yield engine
    engine.dispose()

@pytest.fixture(scope="session")
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()