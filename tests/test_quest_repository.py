import os
import sqlite3
import unittest

from system.database import create_tables
from system.quest import Quest
from system.quest_repository import QuestRepository

TEST_DB_PATH = "test_system.db"


class TestQuestRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(TEST_DB_PATH)
        create_tables(self.connection)
        self.repository = QuestRepository(self.connection)

    def tearDown(self):
        self.connection.close()
        os.remove(TEST_DB_PATH)

    def test_save_and_load_not_started_quest(self):
        quest = Quest("daily_workout", "Complete a workout", 3)
        self.repository.save(quest)

        loaded = self.repository.load("daily_workout")

        self.assertEqual(loaded.name, "Complete a workout")
        self.assertEqual(loaded.reward_points, 3)
        self.assertFalse(loaded.is_completed())

    def test_save_and_load_completed_quest(self):
        quest = Quest("daily_workout", "Complete a workout", 3)
        quest.complete()
        self.repository.save(quest)

        loaded = self.repository.load("daily_workout")

        self.assertTrue(loaded.is_completed())


if __name__ == "__main__":
    unittest.main()