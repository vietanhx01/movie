from fastapi import APIRouter

from model.movie import Movie
from schemas import Movie as MVS

router = APIRouter()
# config.db.connect()

@router.get('/')
def movies():
    return Movie.get_list()

@router.get('/{movie_id}')
def movie(movie_id):
    return Movie.get_movie_by_id(movie_id)

@router.post('/')
def add_movie(mv: MVS):
    mvs_post_data = mv.dict()
    print(mvs_post_data)
    new_movie = Movie.create_movie(mv.dict())
    return new_movie.id

@router.delete('/{movie_id}')
def delete_movie(movie_id):
    delete_rows = Movie.delete_movie(movie_id)
    if delete_rows == 0:
        return False
    return True