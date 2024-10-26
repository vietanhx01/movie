from peewee import TextField, IntegerField, JOIN, fn, \
    ForeignKeyField
from model.seat import Seat
from model.base import BaseModel

class Room(BaseModel):

    room_number = IntegerField(null=False)
    seat_id = ForeignKeyField(Seat, column_name='seat_id')
    capacity = IntegerField(null=False)
    screen_type = TextField(null=False)
    location = TextField(null=False)

    class Meta:
        table_name = "room"

    @classmethod
    def get_rooms_with_seats(cls):
        """query = (
            Room
            .select(Room, Seat)
            .join(Seat, JOIN.LEFT_OUTER, on=(Seat.room_id == Room.id))
            .dicts())"""

        query = cls.select(
            cls.room_number,
            cls.capacity,
            cls.screen_type,
            cls.location,
            fn.jsonb_build_object(
                "seat_id",
                Seat.id,
                "seat_number",
                Seat.seat_number,
                "is_vip",
                Seat.is_vip,
                "is_available",
                Seat.is_available,
            ).alias("seats"),
        ).join(Seat, JOIN.LEFT_OUTER, on=(cls.seat_id == Seat.id)).dicts()

        print(query)
        return list(query)