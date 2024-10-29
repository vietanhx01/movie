from fastapi import APIRouter

from model.room import Room as RoomModel
from model.seat import Seat as SeatModel

router = APIRouter()

@router.get('/')
def rooms():
    return RoomModel.get_rooms_with_seats()

@router.get('/{room_id}')
def seats(room_id):
    return SeatModel.get_seats_by_room(room_id)