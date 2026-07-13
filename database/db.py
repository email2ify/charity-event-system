import sqlite3
from pathlib import Path


# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Database path
DATABASE_PATH = BASE_DIR / "database" / "database.db"


def get_db_connection():
    # Open database
    connection = sqlite3.connect(DATABASE_PATH)

    # Enable rows
    connection.row_factory = sqlite3.Row

    # Enable keys
    connection.execute("PRAGMA foreign_keys = ON")

    # Return connection
    return connection
