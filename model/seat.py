from config import db
from peewee import Model, TextField, IntegerField, ForeignKeyField, BooleanField
from model.base import BaseModel

class Seat(BaseModel):

    seat_number = TextField(null=False)
    is_vip = BooleanField(default=False)
    is_available = BooleanField(default=True)