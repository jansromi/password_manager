import json
import os

class AppConfig:
    """
    This class is responsible for configuring the application.

    On initialization, it tries to find the root directory of the application,
    and config file if it exists. If it does not exist, it creates a default config file.

    @throws: AppRootNotFoundException if cannot determine app root
    """
    CONFIG_PATH = "config/pwm_config.json"

    def __init__(self):
        try:
            self._root_dir = self.find_password_manager_directory()
        except AppRootNotFoundException:
            raise
        
        self._absolute_config_path = os.path.join(self._root_dir, self.CONFIG_PATH)

        try:
            self._config_values = self._get_config_values()
        except AppRootNotFoundException:
            raise
        except FileNotFoundError:
            self.create_default_configuration()

        try:
            # this means we have setup the db before
            self._db_path = self.get_db_path()
        except KeyError:
            self._db_path = self._setup_database_path()

    @property
    def db_path(self):
        return self._db_path

    def _get_config_values(self) -> dict:
        """
        Loads the config file

        @return: config as dict
        """
        try:
            return AppConfig.load_config(self._absolute_config_path)
        except FileNotFoundError:
            raise     

    def save_config_value(self, key: str, value: str, path=None):
        """
        Saves a config value to the config file
        """
        if not path:
            path = self._absolute_config_path
        self._config_values[key] = value
        with open(self._absolute_config_path, 'w') as config_file:
            json.dump(self._config_values, config_file, indent=4)

    def get_config_value(self, key: str) -> str:
        try:
            return self._config_values[key]
        except KeyError:
            raise KeyError(f"Config key {key} not found.")
        

    def create_default_configuration(self):
            """
            Creates a configuration setup for Password Manager.

            Creates a config file in password_manager/config/pwm_config.json
            and creates a bin directory in the root folder
            and saves it's path to the config file.
            """
            self._create_directory(os.path.dirname(self._absolute_config_path))
            self._create_config_file(self._absolute_config_path)
            self._config_values = AppConfig.load_config(self._absolute_config_path)
            bin_dir = os.path.join(self._root_dir, "bin")
            self._create_directory(bin_dir)
            self.save_config_value(key="bin_path", value=bin_dir)

    def _setup_database_path(self):
        bin_dir = self.get_config_value("bin_path")
        db_path = os.path.join(bin_dir, "pwm.db")
        self.save_config_value(key="db_path", value=db_path)
        return db_path

    @staticmethod
    def find_password_manager_directory(starting_directory=".") -> str:
        """
        Traverses up the directory tree until it finds the password_manager directory

        @return: path to password_manager directory
        @throws: AppRootNotFoundException if cannot determine app root
        """
        current_directory = os.path.abspath(starting_directory)

        while current_directory != "/":
            if os.path.isdir(os.path.join(current_directory, "password_manager")):
                return os.path.join(current_directory, "password_manager")

            # Move up a directory
            current_directory = os.path.abspath(os.path.join(current_directory, os.pardir))

        # If the loop completes without finding the directory
        raise AppRootNotFoundException('Could not find password_manager root directory.')
    
    @staticmethod
    def load_config(path: str) -> dict:
        """
        Loads the config file and returns the config as a dictionary

        @return: config as dict
        @throws: FileNotFoundError if cannot find config
        """
        try:
            with open(path) as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find config file at {path}.")

    def _create_directory(self, path: str):
        """
        Creates a directory if it does not exist
        """
        os.makedirs(path, exist_ok=True)

    def _create_config_file(self, path: str):
        """
        Generates a default config file.
        """
        with open(path, 'w') as config_file:
            json.dump({
                "root_folder": self._root_dir
                },
                config_file,
                indent=4)
            
    def get_db_path(self):
        try:
            return self._config_values["db_path"]
        except KeyError:
            raise KeyError("Database path not configured in config file.")
        

class AppRootNotFoundException(Exception):

    def __init__(self, message):
        self.message = message

if __name__ == "__main__":
    config = AppConfig()