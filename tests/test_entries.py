from datetime import datetime
import pytest
from src.core.entry import Entry
from src.core.entries import Entries

def test_get_entry():
    entries = Entries(useDb=False)
    entrydata = {
        'id': 1, 
        'app_name': 'Github',
        'username': 'jansromi',
        'creation_date': '13-12-2023',
        'modified_date': '13-12-2023'
    }
    entry = Entry(**entrydata)
    entries.add_entry(entry)
    result = entries.get_entry(1)
    assert result['app_name'] == 'Github'
    assert result['username'] == 'jansromi'
    assert result['creation_date'] == datetime.strptime('13-12-2023', "%d-%m-%Y")
    assert result['modified_date'] == datetime.strptime('13-12-2023', "%d-%m-%Y")

def test_get_entry_not_found():
    entries = Entries(useDb=False)
    entrydata = {
        'id': 1, 
        'app_name': 'Github',
        'username': 'jansromi',
        'creation_date': '13-12-2023',
        'modified_date': '13-12-2023'
    }
    entry = Entry(**entrydata)
    entries.add_entry(entry)
    
    with pytest.raises(ValueError):
        result = entries.get_entry(2)

def test_add_entry_from_dict():
    entries = Entries(useDb=False)
    entrydata = {
        'id': 1, 
        'app_name': 'Github',
        'username': 'jansromi',
        'creation_date': '13-12-2023',
        'modified_date': '13-12-2023'
    }
    entries.add_entry_from_dict(entrydata)
    result = entries.get_entry(1)
    assert result['app_name'] == 'Github'
    assert result['username'] == 'jansromi'
    assert result['creation_date'] == datetime.strptime('13-12-2023', "%d-%m-%Y")
    assert result['modified_date'] == datetime.strptime('13-12-2023', "%d-%m-%Y")

def test_add_entry_wrong_type():
    entries = Entries(useDb=False)
    entrydata = {
        'id': 1, 
        'app_name': 'Github',
        'username': 'jansromi',
        'creation_date': '13-12-2023',
        'modified_date': '13-12-2023'
    }
    with pytest.raises(TypeError):
        entries.add_entry(entrydata)

    entry = Entry(**entrydata)
    with pytest.raises(TypeError):
        entries.add_entry_from_dict(entry)
