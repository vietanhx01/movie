from fastapi import APIRouter

from model.showtime import Showtime as ShowtimeModel

router = APIRouter()

@router.get('/')
def show_times():
    return ShowtimeModel.get_show_times()