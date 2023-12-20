from core.entry import Entry
from services.database import Database

class Entries:
    
    def __init__(self, useDb=True):
        """
        Initialize the entries class

        @param useDb: if True, setups data in the database
        """
        self._entries = []
        self._db = None
        if useDb:
            self._setup_data()

    def _setup_data(self):
        self._db = Database()
        with self._db:
            self._db.insert_fake_data()
            result = self._db.get_all_entries()
            self._entries = [Entry(**row) for row in result]

    def get_entry(self, index: int) -> dict:
        """
        Iterate through the entries list and return the entry with the given index
        @param index: int-index of the entry
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        for entry in self._entries:
            if entry.id == index:
                return entry.get_entry()
        raise ValueError(f"Entry with index {index} not found")
    
    def add_entry(self, entry: Entry):
        """
        Add an entry to the entries list
        @param entry: Entry-object
        """
        if not isinstance(entry, Entry):
            raise TypeError("Entry must be an Entry-object")
        self._entries.append(entry)

    def add_entry_from_dict(self, entry: dict):
        """
        Add an entry to the entries list
        @param entry: dict
        """
        if not isinstance(entry, dict):
            raise TypeError("Entry must be a dict")
        self._entries.append(Entry(**entry))

    def get_columns(self):
        return self._db.get_column_titles()
    
    def get_entries(self):
        return [entry.to_tuple() for entry in self._entries]