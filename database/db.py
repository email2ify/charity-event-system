import sqlite3
from pathlib import Path


DATABASE_PATH = Path(__file__).with_name("database.db")


def get_db_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
    return connection
