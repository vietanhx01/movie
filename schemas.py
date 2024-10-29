import datetime
from pydantic import BaseModel

class Schema(BaseModel):
    class Config:
        from_attributes = True

class Movie(Schema):
    name: str
    trailer_url: str
    poster_url: str
    description: str
    release_date: datetime.date
    age_rating: int
    duration: int
    genre: str
    director: str
    caster: str
    rating: float
    language: str

class Room(Schema):
    room_number: int
    capacity: int
    screen_type: str
    location: str

class Seat(Schema):
    seat_number: str
    room_id: int
    is_vip: bool
    is_available: bool

class Showtime(Schema):
    movie_id: int
    room_id: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    price: int
