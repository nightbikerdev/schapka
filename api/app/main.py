from fastapi import FastAPI

from app.db.config import Base, async_engine
from app.routers import restaurant

app = FastAPI()

app.include_router(restaurant.router)