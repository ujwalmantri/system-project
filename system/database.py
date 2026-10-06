"""
Sets up the SQLite database and its tabless.
"""

import sqlite3

DB_PATH = "system.db"

def get_connections():
    return sqlite3.connect(DB_PATH)

def create_tables(conneection):
    conneection.execute("""
        CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            level INTEGER NOT NULL,
            ability_points INTEGER NOT NULL,
            strength INTEGER NOT NULL,
            agility INTEGER NOT NULL,
            vitality INTEGER NOT NULL,
            intelligence INTEGER NOT NULL,
            perception INTEGER NOT NULL
        )
    """)
    conneection.commit()