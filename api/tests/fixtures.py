import pytest_asyncio
from app.models.restaurant import Restaurant   

@pytest.fixture
def example_data(db_session):
    # Create example data in the test database
    example_data = [
        Restaurant(id=1, address='address1', lat=1.33, lon=14.1),
        Restaurant(id=2, address='address2', lat=2.33, lon=54.2),
    ]
    db_session.add_all(example_data)
    db_session.commit()
    return example_data