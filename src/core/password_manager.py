from src.core.entries import Entries

class PasswordManager:
    
    def __init__(self):
        self._entries = Entries()

    def get_entry_columns(self) -> list[str]:
        return self._entries.get_columns()
    
    def get_entries(self) -> list[tuple]:
        return self._entries.get_entries()


