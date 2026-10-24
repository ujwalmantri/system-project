"""
Sets up the SQLite database and its tabless.
"""

import sqlite3

DB_PATH = "system.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def create_tables(connection):
    connection.execute("""
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
    connection.execute("""
        CREATE TABLE IF NOT EXISTS quests (
            quest_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            reward_points INTEGER NOT NULL,
            status TEXT NOT NULL
        )
    """)
    connection.execute("""
        CREATE TABLE IF NOT EXISTS streaks (
            id INTEGER PRIMARY KEY,
            current_streak INTEGER NOT NULL,
            longest_streak INTEGER NOT NULL,
            total_completed_days INTEGER NOT NULL,
            last_completed_date TEXT
        )
    """)
    connection.execute("""
        CREATE TABLE IF NOT EXISTS completion_events (
            id INTEGER PRIMARY KEY,
            streak_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            streak_at_completion INTEGER NOT NULL,
            total_completed_days_at_completion INTEGER NOT NULL
        )
    """)
    connection.commit()