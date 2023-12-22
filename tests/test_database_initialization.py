# test_database_initializer.py
import os
import sqlite3
import pytest
from src.services.database_initializer import DatabaseInitializer


@pytest.fixture
def db_path(tmp_path):
    return str(tmp_path / "test.db")

@pytest.fixture
def db_init(db_path):
    return DatabaseInitializer(db_path)

def test_startup_creates_tables(db_init, db_path):
    # The database is initialized
    db_init.startup()

    # Connect to the database and check for tables
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()

    # User and Password tables should exist
    assert "User" in tables
    assert "Password" in tables