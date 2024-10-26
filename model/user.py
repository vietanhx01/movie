import datetime
from config import db
from peewee import Model, AutoField, TextField, DateField, IntegerField, FloatField, PostgresqlDatabase
from model.base import BaseModel


class Director(BaseModel):

    name = TextField(null=False)
    email = TextField(null=False)
    address = TextField(null=False)
    phone = TextField(null=False)
