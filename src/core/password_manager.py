from src.core.entries import Entries
from src.services.app_config import AppConfig

class PasswordManager:
    
    def __init__(self):
        self._app_config = AppConfig()
        self._entries = Entries()

    def get_entry_columns(self) -> list[str]:
        return self._entries.get_columns()
    
    def get_entries(self) -> list[tuple]:
        return self._entries.get_entries()


