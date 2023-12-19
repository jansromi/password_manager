from datetime import datetime

class Entry:
    
    def __init__(self, id: int, app_name: str, username: str, creation_date: str, modified_date: str):
        try:
            self._id = int(id)
        except ValueError:
            raise TypeError("id must be an integer")

        if not app_name:
            raise ValueError("app_name cannot be an empty string")
        self._application_name = app_name

        if not username:
            raise ValueError("username cannot be an empty string")
        self._username = username

        try:
            self._creation_date = datetime.strptime(creation_date, "%d-%m-%Y")
        except ValueError:
            raise ValueError("creation_date must be a string in the format 'dd-mm-yyyy'")

        try:
            self._modified_date = datetime.strptime(modified_date, "%d-%m-%Y")
        except ValueError:
            raise ValueError("modified_date must be a string in the format 'dd-mm-yyyy'")

    @property
    def id(self):
        """
        Return the id of the entry
        """
        return self._id

    def get_entry(self) -> dict:
        """
        Return the entry as a dictionary
        """
        return {
            'id': self._id,
            'app_name': self._application_name,
            'username': self._username,
            'creation_date': self._creation_date,
            'modified_date': self._modified_date
        }
    
    def to_tuple(self) -> tuple:
        """
        Return the entry as a tuple
        """
        return (
            self._application_name,
            self._username,
            self._creation_date,
            self._modified_date
        )

