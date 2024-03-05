from fastapi import FastAPI
from typing import List

from schemas.restaurant import Restaurant

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
def get_restaurant(restaurant_id: int):
    restaurant = Restaurant()
    return restaurant

@app.put("/restaurants/{restaurant_id}", response_model=Restaurant)
def update_restaurant(restaurant_id: int, updated_data: Restaurant):
    current_restaurant = Restaurant()
    return current_restaurant
