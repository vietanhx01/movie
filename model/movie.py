import datetime
from model.director import Director
from peewee import Model, TextField, DateField, IntegerField, FloatField, ForeignKeyField, JOIN, fn

from model.base import BaseModel

class Movie(BaseModel):

    name = TextField(unique=True, null=False)
    trailer_url = TextField(null=False)
    poster_url = TextField(null=False)
    description = TextField(null=False)
    release_date = DateField(null=False, default=datetime.date.today)
    age_rating = IntegerField(null=False)
    duration = IntegerField(null=False)
    genre = TextField(null=False)
    director_id = ForeignKeyField(Director, column_name="director_id")
    caster = TextField(null=False)
    rating = FloatField(null=False)
    language = TextField(null=False)

    @classmethod
    def get_list(cls):
        query = cls.select(
            cls.name,
            cls.poster_url,
            cls.release_date,
            cls.age_rating,
            cls.genre,
            cls.rating,
            # Director.name.alias('director_name'),
            fn.jsonb_build_object(
                "id",
                Director.id,
                "name",
                Director.name,
                "mail",
                Director.mail,
                "address",
                Director.address,
                "phone",
                Director.phone,
            ).alias("director"),
        ).join(Director, JOIN.LEFT_OUTER, on=cls.director_id==Director.id).dicts()

        print(query)
        return list(query)

    @classmethod
    def get_list_by_id(cls, id):
        query = cls.select().where(cls.id == id).dicts()
        return list(query)

    @classmethod
    def create_movie(cls, movie_data: dict):
        # movie = cls.create(
        #     name=movie_data['name'],
        #     trailer_url=movie_data['trailer_url'],
        #     poster_url=movie_data['poster_url'],
        #     description=movie_data['description'],
        #     release_date=movie_data['release_date'],
        #     duration=movie_data['duration'],
        #     genre=movie_data['genre'],
        #     director=movie_data['director'],
        #     caster=movie_data['caster'],
        #     rating=movie_data['rating'],
        #     language=movie_data['language']
        # )
        movie = cls.create(**movie_data)
        return movie

    @classmethod
    def delete_movie(cls, movie_id: int):
        query = cls.delete().where(cls.id == movie_id)
        deleted_rows = query.execute()
        return deleted_rows