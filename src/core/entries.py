from src.utils.gen_fake_data import generate_fake_data 
from src.core.entry import Entry

class Entries:
    
    def __init__(self):
        self._entries = []

    def set_fake_data(self):
        data = generate_fake_data(10)
        for row in data:
            self._entries.append(Entry(**row))

    def get_entry(self, index):
        for entry in self._entries:
            if entry.get_id() == index:
                return entry.get_entry()
        return None
    
    def add_entry(self, entry):
        self._entries.append(entry)
