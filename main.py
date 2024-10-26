from fastapi import FastAPI

from model.movie import Movie
from model.room import Room as RoomModel
import config
from schemas import Movie as MVS

app = FastAPI()

config.db.connect()

@app.get('/')
def movies():
    return Movie.get_list()

@app.post('/add/')
def add_movie(mv: MVS):
    mvs_post_data = mv.dict()
    print(mvs_post_data)
    new_movie = Movie.create_movie(mv.dict())
    return new_movie.id

@app.delete('/movies/{movie_id}')
def delete_movie(movie_id):
    delete_rows = Movie.delete_movie(movie_id)
    if delete_rows == 0:
        return False
    return True

@app.get('/rooms')
def rooms():
    return RoomModel.select()