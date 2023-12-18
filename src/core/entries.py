from src.utils.gen_fake_data import generate_fake_data 
from src.core.entry import Entry

class Entries:
    
    def __init__(self):
        self._entries = []
        self.set_fake_data()

    def set_fake_data(self):
        data = generate_fake_data(10)
        for row in data:
            self._entries.append(Entry(**row))

    def get_entry(self, index):
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
        return ["application name", "username", "created", "last updated"]
    
    def get_entries(self):
        return [entry.to_tuple() for entry in self._entries]