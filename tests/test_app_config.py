import os
import shutil
import subprocess

"""
The purpose of this test file is to examine how the AppConfig class behaves in normal and exceptional situations.

The reason for testing is the desire to understand whether the program can be gracefully shut down,
for example, in scenarios where the root directory of the application is maliciously manipulated.


Author: jansromi
Date: 20.12.2023
"""

def test_app_config_execution(setup_temp_dir):
    result = subprocess.run(["python3", "src/services/app_config.py"], cwd=setup_temp_dir, capture_output=True, text=True)
    assert result.returncode == 0
    assert result.stdout == ""

def test_app_config_modified_directory_name(setup_misnamed_temp_dir):
        """
        Test if app raises AppRootNotFoundException
        when wrong directory name is used
        """
        result = subprocess.run(["python3", "src/services/app_config.py"], cwd=setup_misnamed_temp_dir, capture_output=True, text=True)
        # Check if we have a correct exception in stderr.
        # Feeling very sus about this assertion,
        # but have not figured out a better way to do it yet.
        assert "AppRootNotFoundException" in result.stderr, "AppRootNotFoundException not found in stderr"

def test_app_config_setups_without_config(setup_temp_dir):
    """
    Test if config app setups without config file and bin directory.
    Deletes the config file and bin directory before the test.
    AppConfig should create the config file and bin directory on 
    initialization.
    """
    shutil.rmtree(os.path.join(setup_temp_dir, "bin"))
    shutil.rmtree(os.path.join(setup_temp_dir, "config"))

    result = subprocess.run(["python3", "src/services/app_config.py"], cwd=setup_temp_dir, capture_output=True, text=True)

    assert os.path.isdir(os.path.join(setup_temp_dir, "bin")), "Expected AppConfig to create a 'bin' directory, but it was not found"
    assert os.path.isdir(os.path.join(setup_temp_dir, "config")), "Expected AppConfig to create a 'config' directory, but it was not found"

    assert result.returncode == 0
    assert result.stdout == ""
    


