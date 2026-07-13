from db import get_db_connection

connection = get_db_connection()

cursor = connection.cursor()

# Create Event table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Event (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_name TEXT NOT NULL,
    event_date TEXT NOT NULL,
    location TEXT NOT NULL,
    description TEXT
)
""")

# Create Registration table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Registration (
    registration_id INTEGER PRIMARY KEY AUTOINCREMENT,
    participant_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    registration_date TEXT NOT NULL,
    event_id INTEGER NOT NULL,
    FOREIGN KEY(event_id) REFERENCES Event(event_id)
)
""")
cursor.execute("""
INSERT OR IGNORE INTO Event
(event_id, event_name, event_date, location, description)

VALUES
(
1,
'Charity Fun Run',
'2026-09-15',
'Campus Park',
'Annual charity fundraising event supporting local community projects.'
)
""")
connection.commit()
connection.close()

print("Database created successfully.")