import sqlite3

class DatabaseInitializer:
    tables = ["User", "Password"]

    def __init__(self, db_path):
        self._db_path = db_path

    def startup(self):
        """
        Checks if database tables exisit
        """
        for table in self.tables:
            if not self._table_exists(table):
                self._create_tables()

    def _table_exists(self, table_name) -> bool:
        connection = sqlite3.connect(self._db_path)
        cursor = connection.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        result = cursor.fetchone()
        connection.close()
        return result is not None
    
    def _create_tables(self):
        connection = sqlite3.connect(self._db_path)
        cursor = connection.cursor()
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS User (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    masterkey_hash TEXT NOT NULL,
                    device_secret TEXT NOT NULL,
                    creation_date DATE,
                    modified_date DATE
                )
            ''')
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Password (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    application_name TEXT NOT NULL,
                    encrypted_password TEXT NOT NULL,
                    creation_date DATE,
                    modified_date DATE,
                    FOREIGN KEY (user_id) REFERENCES User (id)
                )
            ''')
        connection.commit()