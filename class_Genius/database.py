import sqlite3

conn = sqlite3.connect("classgenius.db", check_same_thread=False)
c = conn.cursor()

# Users table
c.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT,
    role TEXT
)
''')

# Notes table (NO DUPLICATES)
c.execute('''
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT UNIQUE
)
''')

# Default users
c.execute("INSERT OR IGNORE INTO users VALUES ('admin','admin123','admin')")
c.execute("INSERT OR IGNORE INTO users VALUES ('student','student123','student')")

conn.commit()
