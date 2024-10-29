from peewee import TextField
from model.base import BaseModel

class Director(BaseModel):

    name = TextField(null=False)
    email = TextField(null=False)
    address = TextField(null=False)
    phone = TextField(null=False)
