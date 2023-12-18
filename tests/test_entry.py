from datetime import datetime
from src.core.entry import Entry

def test_entry_initialization():
    entrydata = {
        'id': '1', 
        'app_name': 'Github',
        'username': 'jansromi',
        'creation_date': '13-12-2023',
        'modified_date': '13-12-2023'
    }
    entry = Entry(**entrydata)
    result = entry.get_entry()
    assert result['app_name'] == 'Github'
    assert result['username'] == 'jansromi'
    assert result['creation_date'] == datetime.strptime('13-12-2023', "%d-%m-%Y")
    assert result['modified_date'] == datetime.strptime('13-12-2023', "%d-%m-%Y")
