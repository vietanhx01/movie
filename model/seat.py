from dns.e164 import query
from peewee import Model, TextField, IntegerField, ForeignKeyField, BooleanField
from model.base import BaseModel
from model.room import Room

class Seat(BaseModel):

    seat_number = TextField(null=False)
    room_id = ForeignKeyField(Room, column_name='room_id')
    is_vip = BooleanField(default=False)
    is_available = BooleanField(default=True)

    @classmethod
    def get_seats_by_room(cls, room_id):
        query = cls.select().where(cls.room_id == room_id).dicts()
        return list(query)