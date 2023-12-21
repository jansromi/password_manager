import sys

from src.core.entries import Entries
from src.services.app_config import AppConfig, AppRootNotFoundException
from src.services.database import Database
from src.services.database_initializer import DatabaseInitialzer

class PasswordManager:
    
    def __init__(self):
        try:
            self._app_config = AppConfig()
        except AppRootNotFoundException:
            # app not found, exit
            sys.exit(4)
        database_initializer = DatabaseInitialzer(self._app_config.db_path)
        database_initializer.startup()
        db = Database(self._app_config.db_path)
        self._entries = Entries(database_instance=db, use_fake_data=True)

    def get_entry_columns(self) -> list[str]:
        return self._entries.get_columns()
    
    def get_entries(self) -> list[tuple]:
        return self._entries.get_entries()


