from peewee import TextField, IntegerField, JOIN, fn
from model.base import BaseModel

class Room(BaseModel):

    room_number = IntegerField(null=False)
    capacity = IntegerField(null=False)
    screen_type = TextField(null=False)
    location = TextField(null=False)

    @classmethod
    def get_rooms_with_seats(cls):
        from model.seat import Seat
        """query = (
            Room
            .select(Room, Seat)
            .join(Seat, JOIN.LEFT_OUTER, on=(Seat.room_id == Room.id))
            .dicts())"""

        query = cls.select(
            cls.id,
            cls.room_number,
            cls.capacity,
            cls.screen_type,
            cls.location,
            fn.jsonb_build_object(
                "seat_id",
                Seat.id,
                "seat_number",
                Seat.seat_number,
                "room_id",
                Seat.room_id,
                "is_vip",
                Seat.is_vip,
                "is_available",
                Seat.is_available,
            ).alias("seats"),
        ).join(Seat, JOIN.RIGHT_OUTER, on=(cls.id == Seat.room_id)).dicts()

        print(query)
        return list(query)