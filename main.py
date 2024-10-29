from fastapi import FastAPI
from config import database
from core.v1.api import api_router

app = FastAPI()
database.db.connect()
app.include_router(api_router)
