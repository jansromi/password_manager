from datetime import datetime

class Entry:
    def __init__(self, **kwargs):
        self._application_name = kwargs.get('app_name', '')
        self._username = kwargs.get('username', '')
        self._creation_date = datetime.strptime(kwargs.get('creation_date', ''), "%d.%m.%Y")
        self._modified_date = datetime.strptime(kwargs.get('modified_date', ''), "%d.%m.%Y")

    def get_entry(self):
        return {
            'app_name': self._application_name,
            'username': self._username,
            'creation_date': self._creation_date,
            'modified_date': self._modified_date
        }

