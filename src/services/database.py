import os
import json
import sqlite3

class Database:
    """
    This class handles all database related operations.

    Currently it also handles the creation of the database and the config file,
    so later this should be moved to a separate class.

    The database and config are created in the bin directory if they don't exist.

    Class should be used as a context manager, ie.:
        db = DbHandler()
        with db:
            db.insert_fake_data()
            db.commit() 
    """
    DB_NOT_FOUND = None

    def __init__(self):
        self.config = self.load_config()
        self.db_path = os.path.join(self.config["db_directory"], self.config["db_name"])
        if Database.DB_NOT_FOUND:
            self.create_tables()
        self.conn = None
        self.cursor = None

    def load_config(self):
        """Loads the config file and returns the config as a dictionary"""
        try:
            # find path this code is executing in
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # go two directories up, ie. projectroot.
            # heavy assumpions here about project structure
            # TODO: make this more robust (recursion?)
            parent_dir = os.path.dirname(script_dir)
            parent_dir = os.path.dirname(parent_dir)

            # ie. projectroot/bin
            bin_dir = os.path.join(parent_dir, 'bin')
            # if there is a config-file, it should be in bin directory
            config_path = os.path.join(bin_dir, 'config.json')
            # if config doesn't exist, create it
            if not os.path.exists(config_path):
                config = {
                    "db_directory": str(bin_dir),
                    "db_name": "password_manager.db"
                }
                # create bin directory if it doesn't exist
                if not os.path.exists(bin_dir):
                    os.makedirs(bin_dir, exist_ok=True)
                    # if bin directory didn't exist, there is also no database
                    Database.DB_NOT_FOUND = True
                # create config file
                with open(config_path, 'x') as f:
                    json.dump(config, f, indent=4)
            with open(config_path, 'r') as f:
                # and return it
                return json.load(f)

        except Exception as e:
            print(f"Error loading config file: {e}")
            
    def __enter__(self):
        if not self.db_path:
            # because init is called before __enter__, this should never happen
            pass
        self.conn = sqlite3.connect(self.db_path)
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

    def insert_fake_data(self):
        self.cursor.execute('''
            INSERT INTO User (username, pword_hash, salt, creation_date, modified_date)
            VALUES ("Roba", "poary442jbqi", "08vc2xlys3", "12.12.2023", "12.12.2023"),
                    ("Jansromi", "1avm38gkj24", "08vc2xlys3", "12.12.2023", "12.12.2023"),
                    ("Jansromi2", "1avm38gkj24", "08vc2xlys3", "12.12.2023", "12.12.2023")
        ''')
        self.cursor.execute('''
            INSERT INTO Password (user_id, application_name, pword_hash, creation_date, modified_date)
            VALUES (1, "facebook", "1avm38gkj24", "12.12.2023", "12.12.2023"),
                    (2, "twitter", "1avm38gkj24", "12.12.2023", "12.12.2023"),
                    (1, "instagram", "1avm38gkj24", "12.12.2023", "12.12.2023")
        ''')
    
    def get_fake_columns(self):
        return ['application_name', 'username', 'password']

    def get_fake_values(self):
        return [
            ('Facebook', 'IamRoba', '12345'),
            ('Instagram', 'Roba', '54321'),
            ('Steam', 'Roba', '12345')]


# Example usage
""" db = DbHandler()
with db:
    db.insert_fake_data()
    db.commit_and_close() """
