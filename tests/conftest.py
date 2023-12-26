import os
import shutil
import pytest
from src.services.app_config import AppConfig

def copy_dir_to_temp_dir(pwm_dir, tmp_dir):
    """
    Copy the project directory to a temporary directory
    """
    original_dir = os.getcwd()

    # Copies password manager directory to temporary directory
    shutil.copytree(pwm_dir, tmp_dir)

    # Change inside the tmp directory
    os.chdir(tmp_dir)

    return original_dir

def cleanup(tmp_dir, original_dir):
    os.chdir(original_dir)
    shutil.rmtree(tmp_dir)

@pytest.fixture
def setup_temp_dir(tmp_path):
    """
    Fixture setups a directory and removes it after the test
    """
    temp_dir = tmp_path / "password_manager"
    original_dir = copy_dir_to_temp_dir(AppConfig.find_password_manager_directory(), temp_dir)

    yield str(temp_dir)

    cleanup(str(temp_dir), original_dir)

@pytest.fixture
def setup_misnamed_temp_dir(tmp_path):
    """
    Fixture setups a misnamed directory and removes it after the test
    """
    temp_dir = tmp_path / "passwordmanager"
    original_dir = copy_dir_to_temp_dir(AppConfig.find_password_manager_directory(), temp_dir)

    yield str(temp_dir)

    cleanup(str(temp_dir), original_dir)