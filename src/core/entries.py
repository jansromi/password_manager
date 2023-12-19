from src.utils.gen_fake_data import generate_fake_data 
from src.core.entry import Entry
from src.services.database import Database

class Entries:
    
    def __init__(self, testing=False):
        self._entries = []
        if not testing:
            self._db = Database()
            result = None
            with self._db:
                self._db.insert_fake_data()
                result = self._db.get_all_entries()
                for row in result:
                    self._entries.append(Entry(**row))
        else:
            pass

    def get_entry(self, index: int):
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        for entry in self._entries:
            if entry.get_id() == index:
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