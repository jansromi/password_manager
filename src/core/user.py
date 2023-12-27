from src.core.entries import Entries
from src.core.password import Password

class User:
    def __init__(self, id: int, entries: Entries, password: Password) -> None:
        self._id = id
        self._entries = entries
        self._password = password