import os
import sqlite3
from src.services.app_config import AppConfig

class Database:
    """
    This class handles all database related operations.

    Class should be used as a context manager, ie.:
        db = DbHandler()
        with db:
            db.insert_fake_data()
            db.commit() 
    """

    def __init__(self):
        self._appconf = AppConfig()
        try:
            self._db_path = self._appconf.get_db_path()
        except KeyError:
            self._db_path = self.setup()
            self.create_tables()
            self._appconf.save_config_value(key="db_path", value=self._db_path)
        self.conn = None
        self.cursor = None
    
    def setup(self):
        bin_dir = self._appconf.get_config_value("bin_path")
        db_path = os.path.join(bin_dir, "pwm.db")
        self._appconf.save_config_value(key="db_path", value=db_path)
        return db_path

    def __enter__(self):
        if not self._db_path:
            pass

        self.conn = sqlite3.connect(self._db_path)
        self.cursor = self.conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.close()

    def commit(self):
        if self.conn:
            self.conn.commit()

    def create_tables(self):
        with self:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS User (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    pword_hash TEXT NOT NULL,
                    salt TEXT NOT NULL,
                    creation_date DATE NOT NULL,
                    modified_date DATE NOT NULL
                )
            ''')
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Password (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    application_name TEXT NOT NULL,
                    pword_hash TEXT NOT NULL,
                    creation_date DATE NOT NULL,
                    modified_date DATE NOT NULL,
                    FOREIGN KEY (user_id) REFERENCES User (id)
                )
            ''')
            self.conn.commit()

    def get_column_titles(self):
        return ['application name', 'username', 'password', 'modified date']

    def insert_fake_data(self):
        self.cursor.execute('''
        INSERT INTO User (username, pword_hash, salt, creation_date, modified_date)
        VALUES ("Roba", "poary442jbqi", "08vc2xlys3", "2023-12-12", "2023-12-12"),
                ("Jansromi", "1avm38gkj24", "08vc2xlys3", "2023-12-12", "2023-12-12"),
                ("rrobe", "1avm38gkj24", "08vc2xlys3", "2023-12-12", "2023-12-12")
        ''')
        self.cursor.execute('''
        INSERT INTO Password (user_id, application_name, pword_hash, creation_date, modified_date)
        VALUES (1, "facebook", "1avm38gkj24", "2023-12-12", "2023-12-12"),
                (2, "twitter", "1avm38gkj24", "2023-12-12", "2023-12-12"),
                (1, "instagram", "1avm38gkj24", "2023-12-12", "2023-12-12"),
                (3, "twitch", "1avm38gkj24", "2023-12-12", "2023-12-12"),
                (1, "github", "1avm38gkj24", "2023-12-12", "2023-12-12"),
                (2, "google", "1avm38gkj24", "2023-12-12", "2023-12-12")
        ''')


    def get_all_entries(self):
        '''
        Return all found entries in the database

        @return: list of tuples
        '''
        self.cursor.execute('''
            SELECT
                Password.id,
                Password.application_name,
                User.username,
                strftime('%d-%m-%Y', Password.creation_date) AS password_creation_date,
                strftime('%d-%m-%Y', Password.modified_date) AS password_modified_date
            FROM
                Password
            JOIN
                User ON Password.user_id = User.id;

        ''')
        result = self.cursor.fetchall()
        entries_data = [
            {
                'id': row[0],
                'app_name': row[1],
                'username': row[2],
                'creation_date': row[3],
                'modified_date': row[4]
            }
            for row in result
        ]
        return entries_data