from contextvars import ContextVar

import peewee

POSTGRES_USER = 'admin'
POSTGRES_PASS = 'Password@1234'
POSTGRES_DB = 'cinema'
POSTGRES_PORT = '2345'
POSTGRES_HOST = 'localhost'

db_state_default = {"closed": None, "conn": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())

class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.PostgresqlDatabase(
    POSTGRES_DB, user = POSTGRES_USER, password=POSTGRES_PASS, host=POSTGRES_HOST, port=POSTGRES_PORT
)

db._state = PeeweeConnectionState()