import pytest
from api.models.restaurant import Restaurant   

@pytest.fixture
def example_data(db_session):
    # Create example data in the test database
    example_data = [
        Restaurant(id=1, address='address', lat=3.33, lon=44.4),
        Restaurant(field1='value3', field2='value4'),
        # Add more example data as needed
    ]
    db_session.add_all(example_data)
    db_session.commit()
    return example_data