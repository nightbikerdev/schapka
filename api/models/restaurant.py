from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    lat = Column(Float)
    lon = Column(Float)

    def __repr__(self):
        return f"<Restaurant(name='{self.name}', address ='{self.address}', lat='{self.lat}', lon='{self.lon}')>"
