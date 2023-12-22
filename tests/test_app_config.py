import os
import shutil
import subprocess
import pytest
from src.services.app_config import AppConfig

"""
The purpose of this test file is to examine how the AppConfig class behaves in normal and exceptional situations.

The reason for testing is the desire to understand whether the program can be gracefully shut down,
for example, in scenarios where the root directory of the application is maliciously manipulated.


Author: jansromi
Date: 20.12.2023
"""

TMP_DIR_PATH = "/tmp/testing/password_manager"

def copy_directory(tmp_dir):
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
def copy_dir():
    """
    Fixture setups a directory and removes it after the test
    """
    original_dir = copy_directory(TMP_DIR_PATH)

    yield TMP_DIR_PATH

    cleanup(TMP_DIR_PATH, original_dir)

@pytest.fixture
def copy_wrongly_named_dir():

    path_parts = TMP_DIR_PATH.split(os.path.sep)
    path_parts[-1] = "passwordmanager"
    bad_path = os.path.join("/", *path_parts)

    original_dir = copy_directory(bad_path)

    yield bad_path

    cleanup(bad_path, original_dir)

def test_app_config_execution(copy_dir):
    result = subprocess.run(["python3", "src/services/app_config.py"], cwd=copy_dir, capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout == ""

def test_app_config_modified_directory_name(copy_wrongly_named_dir):
        """
        Test if app raises AppRootNotFoundException
        when wrong directory name is used
        """
        result = subprocess.run(["python3", "src/services/app_config.py"], cwd=copy_wrongly_named_dir, capture_output=True, text=True)
        # Check if we have a correct exception in stderr.
        # Feeling very sus about this assertion,
        # but have not figured out a better way to do it yet.
        assert "AppRootNotFoundException" in result.stderr, "AppRootNotFoundException not found in stderr"

def test_app_config_setups_without_config(copy_dir):
    """
    Test if config app setups without config file and bin directory.
    Deletes the config file and bin directory before the test.
    AppConfig should create the config file and bin directory on 
    initialization.
    """
    shutil.rmtree(os.path.join(copy_dir, "bin"))
    shutil.rmtree(os.path.join(copy_dir, "config"))

    result = subprocess.run(["python3", "src/services/app_config.py"], cwd=copy_dir, capture_output=True, text=True)

    assert os.path.isdir(os.path.join(copy_dir, "bin")), "bin directory was not found"
    assert os.path.isdir(os.path.join(copy_dir, "config")), "config directory was not found"

    assert result.returncode == 0
    assert result.stdout == ""
    


