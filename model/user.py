from peewee import TextField
from model.base import BaseModel

class User(BaseModel):

    name = TextField(null=False)
    email = TextField(null=False)
    address = TextField(null=False)
    phone = TextField(null=False)

    @classmethod
    def add_user(cls, user_data: dict):
        user = cls.create(**user_data)
        return user

    @classmethod
    def get_users(cls):
        query = cls.select(
            cls.id,
            cls.name,
            cls.email,
            cls.address,
            cls.phone).dicts()
        return list(query)

    @classmethod
    def delete_user(cls, user_id: int):
        query = cls.delete().where(cls.id == user_id)
        delete_rows = query.execute()
        return delete_rows