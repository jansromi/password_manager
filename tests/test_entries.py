from datetime import datetime
from src.core.entry import Entry
from src.core.entries import Entries


def test_get_entry():
    entries = Entries()
    entrydata = {
        'id': '1', 
        'app_name': 'Github',
        'username': 'jansromi',
        'creation_date': '13.12.2023',
        'modified_date': '13.12.2023'
    }
    entry = Entry(**entrydata)
    entries.add_entry(entry)
    print(entrydata['creation_date'])
    result = entries.get_entry('1')
    assert result['app_name'] == 'Github'
    assert result['username'] == 'jansromi'
    assert result['creation_date'] == datetime.strptime('13.12.2023', "%d.%m.%Y")
    assert result['modified_date'] == datetime.strptime('13.12.2023', "%d.%m.%Y")

def test_get_entry_not_found():
    entries = Entries()
    entrydata = {
        'id': '1', 
        'app_name': 'Github',
        'username': 'jansromi',
        'creation_date': '13.12.2023',
        'modified_date': '13.12.2023'
    }
    entry = Entry(**entrydata)
    entries.add_entry(entry)
    result = entries.get_entry('2')
    assert result is None