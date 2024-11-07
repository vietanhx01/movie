from fastapi import APIRouter

from model.showtime import Showtime as ShowtimeModel
from schemas import Showtime as ShowTimeSchemas

router = APIRouter()

@router.get('/')
def show_times():
    return ShowtimeModel.get_show_times()

@router.post('/')
def add_show_time(st: ShowTimeSchemas):
    new_show_time = ShowtimeModel.add_show_time(st.dict())
    return new_show_time.id