from pydantic import BaseModel

class Restaurant(BaseModel):
    name: str
    description: str = None
    rating: float
