from fastapi import APIRouter
from core.v1.movie import movie
from core.v1.room import room
from core.v1.showtime import showtime
api_router = APIRouter()

api_router.include_router(movie.router, prefix="/movies", tags=["Movie"])

api_router.include_router(room.router, prefix="/rooms", tags=["Room"])

api_router.include_router(showtime.router, prefix="/showtimes", tags=["Showtime"])