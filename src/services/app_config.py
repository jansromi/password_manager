

import json
import os


class AppConfig:
    """
    
    """
    CONFIG_PATH = "config/pwm_config.json"

    def __init__(self):
        try:
            self._config = self._get_config()
            # TODO: db, bin folder etc
        except AppRootNotFoundException:
            raise

    def _get_config(self) -> dict:
        """
        Loads the config file

        @return: config as dict
        @throws: AppRootNotFoundException if cannot determine app root
        """
        # try to find app root
        try:
            self._root_dir = AppConfig.find_password_manager_directory()

        except AppRootNotFoundException:
            # this can happen when project folder is named something else
            # than password manager
            raise
        
        # config location is set at
        # password_manager/config/pwm_config.json
        config_path = os.path.join(self._root_dir, "config/pwm_config.json")

        try:
            return AppConfig.load_config(config_path)
        except FileNotFoundError:
            # create config with default values
            self.create_config(config_path)
            return AppConfig.load_config(config_path)        

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

    def create_config(self, path: str):
        config_dir = os.path.dirname(path)
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)

        with open(path, 'w') as config_file:
            json.dump({
                "root_folder": self._root_dir
                },
                config_file,
                indent=4) 


class AppRootNotFoundException(Exception):

    def __init__(self, message):
        self.message = message

ap = AppConfig()