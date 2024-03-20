import uuid
from typing import List
from fastapi import APIRouter
from schemas.restaurant import Restaurant, MealRequest, MealResponse, MealUpdate, ReviewMeal

router = APIRouter(prefix="/restaurants")

@router.get("/")
def read_root():
    return {"Hello": "Schapka"}

@router.post("/", response_model=Restaurant)
def create_restaurant(restaurant: Restaurant):
    return restaurant

@router.get("/restaurants", response_model=List[Restaurant])
def get_restaurants():
    return list()

@router.get("/{restaurant_id}", response_model=Restaurant)
def get_restaurant(restaurant_id: uuid.UUID):
    restaurant = Restaurant()
    return restaurant

@router.put("/{restaurant_id}", response_model=Restaurant)
def update_restaurant(restaurant_id: uuid.UUID, updated_data: Restaurant):
    current_restaurant = Restaurant()
    return current_restaurant

@router.post("/meals")
def create_meal(meal: MealRequest):
    pass

@router.get("/meals", response_model=List[MealResponse])
def get_meals():
    return list()

@router.get("/meals/{meal_id}", response_model=MealResponse)
def get_meal(meal_id: uuid.UUID):
    restaurant = Restaurant()
    return restaurant

@router.put("/meals/{meal_id}", response_model=MealResponse)
def update_meal(meal_id: uuid.UUID, updated_data: MealUpdate):
    current_meal = MealResponse()
    return current_meal

@router.post("/review/{restaurant_id}/{meal_id}")
def review_meal(restaurant_id: uuid.UUID, meal_id: uuid.UUID, review: ReviewMeal):
    return {"message": "Review added successfully"}
