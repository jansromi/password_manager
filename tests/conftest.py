import os
import shutil
import pytest
from src.services.app_config import AppConfig

"""
FModule for pytest fixtures.
"""

TMP_DIR_PATH = "/tmp/testing/password_manager"

def copy_dir_to_temp_dir(tmp_dir):
    """
    Copy the project directory to a temporary directory
    """
    original_dir = os.getcwd()
    pwm_dir = AppConfig.find_password_manager_directory()

    # Copies password manager directory to temporary directory
    shutil.copytree(pwm_dir, tmp_dir)

    # Change inside the tmp directory
    os.chdir(tmp_dir)

    return original_dir

def cleanup(tmp_dir, original_dir):
    os.chdir(original_dir)
    shutil.rmtree(tmp_dir)
    # remove /testing from /tmp
    os.rmdir(os.path.dirname(tmp_dir))

@pytest.fixture
def setup_temp_dir():
    """
    Fixture setups a directory and removes it after the test
    """
    original_dir = copy_dir_to_temp_dir(TMP_DIR_PATH)

    yield TMP_DIR_PATH

    cleanup(TMP_DIR_PATH, original_dir)

@pytest.fixture
def setup_misnamed_temp_dir():
    """
    Fixture setups a misnamed directory and removes it after the test
    """
    path_parts = TMP_DIR_PATH.split(os.path.sep)
    path_parts[-1] = "passwordmanager"
    bad_path = os.path.join("/", *path_parts)

    original_dir = copy_dir_to_temp_dir(bad_path)

    yield bad_path

    cleanup(bad_path, original_dir)