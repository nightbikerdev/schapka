import uuid

from fastapi import FastAPI
from typing import List

from schemas.restaurant import Restaurant, MealRequest, MealResponse, MealUpdate, ReviewMeal

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Schapka"}

@app.post("/restaurants", response_model=Restaurant)
def create_restaurant(restaurant: Restaurant):
    return restaurant

@app.get("/restaurants", response_model=List[Restaurant])
def get_restaurants():
    return list()

@app.get("/restaurants/{restaurant_id}", response_model=Restaurant)
def get_restaurant(restaurant_id: uuid.UUID):
    restaurant = Restaurant()
    return restaurant

@app.put("/restaurants/{restaurant_id}", response_model=Restaurant)
def update_restaurant(restaurant_id: uuid.UUID, updated_data: Restaurant):
    current_restaurant = Restaurant()
    return current_restaurant

@app.post("/meals")
def create_meal(meal: MealRequest):
    pass

@app.get("/meals", response_model=List[MealResponse])
def get_meals():
    return list()

@app.get("/meals/{meal_id}", response_model=MealResponse)
def get_meal(meal_id: uuid.UUID):
    restaurant = Restaurant()
    return restaurant

@app.put("/meals/{meal_id}", response_model=MealResponse)
def update_meal(meal_id: uuid.UUID, updated_data: MealUpdate):
    current_meal = MealResponse()
    return current_meal

@app.post("/review/{restaurant_id}/{meal_id}")
def review_meal(restaurant_id: uuid.UUID, meal_id: uuid.UUID, review: ReviewMeal):
    return {"message": "Review added successfully"}
