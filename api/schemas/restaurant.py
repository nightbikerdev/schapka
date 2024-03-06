import uuid
from pydantic import BaseModel, UUID4

class Restaurant(BaseModel):
    name: str
    description: str = None
    rating: float

class ReviewMeal(BaseModel):
    review: str

class MealRequest(BaseModel):
    restaurant_id: uuid.UUID
    name: str
    review: ReviewMeal

class MealResponse(BaseModel):
    restaurant_id: uuid.UUID
    name: str
    review: ReviewMeal    

class MealUpdate(BaseModel):
    restaurant_id: uuid.UUID
    name: str
    review: ReviewMeal  
