from model.movie import Movie
from model.room import Room
from peewee import DateTimeField, IntegerField, JOIN, fn, ForeignKeyField
from model.base import BaseModel

class Showtime(BaseModel):

    movie_id = ForeignKeyField(Movie, column_name='movie_id')
    room_id = ForeignKeyField(Room, column_name='room_id')
    start_time = DateTimeField(null=False)
    end_time = DateTimeField(null=False)
    price = IntegerField(null=False)

    @classmethod
    def add_show_time(cls, show_time_data: dict):
        show_time = cls.create(**show_time_data)
        return show_time


    @classmethod
    def get_show_times(cls):
        query = cls.select(
            fn.jsonb_build_object(
                "name", Movie.name,
                "duration", Movie.duration,
                "genre", Movie.genre
            ).alias("movie"),
            fn.jsonb_build_object(
                "room_number", Room.room_number,
                "screen_type", Room.screen_type
            ).alias("room"),
        ).join(Movie, JOIN.INNER, on=(cls.movie_id == Movie.id)) \
         .join(Room, JOIN.INNER, on=(cls.room_id == Room.id)) \
        .dicts()

        print(query)
        return list(query)