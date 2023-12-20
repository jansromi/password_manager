import sys
from core.entries import Entries
from services.app_config import AppConfig, AppRootNotFoundException

class PasswordManager:
    
    def __init__(self):
        try:
            self._app_config = AppConfig()
        except AppRootNotFoundException:
            # app not found, exit
            sys.exit(1)
        self._entries = Entries()

    def get_entry_columns(self) -> list[str]:
        return self._entries.get_columns()
    
    def get_entries(self) -> list[tuple]:
        return self._entries.get_entries()


