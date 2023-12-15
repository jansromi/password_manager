from utils import gen_fake_data as gen
from core.entry import Entry
class Entries:
    
    def __init__(self):
        self._entries = []
        data = gen.generate_fake_data(10)
        for row in data:
            self._entries.append(Entry(**row))