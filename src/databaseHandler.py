import sqlite3

class DatabaseHandler:
    def __init__(self):
        #self.db_path = db_path
        #self.conn = None
        #self.cursor = None
        pass

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def create_user_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS User (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                pword_hash TEXT NOT NULL,
                salt TEXT NOT NULL,
                creation_date TEXT NOT NULL,
                modified_date TEXT NOT NULL
            )
        ''')

    def create_password_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Password (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                application_name TEXT NOT NULL,
                pword_hash TEXT NOT NULL,
                creation_date TEXT NOT NULL,
                modified_date TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES User (id)
            )
        ''')

    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()

    def get_fake_columns(self):
        return ['application_name', 'username', 'password']

    def get_fake_values(self):
        return [
            ('Facebook', 'IamRoba', '12345'),
            ('Instagram', 'Roba', '54321'),
            ('Steam', 'Roba', '12345')]

