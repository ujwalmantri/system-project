import os
import sqlite3
import unittest
from datetime import date

from system.database import create_tables
from system.streak_tracker import StreakTracker
from system.streak_tracker_repository import StreakTrackerRepository

TEST_DB_PATH = "test_system.db"


class TestStreakTrackerRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(TEST_DB_PATH)
        create_tables(self.connection)
        self.repository = StreakTrackerRepository(self.connection)

    def tearDown(self):
        self.connection.close()
        os.remove(TEST_DB_PATH)

    def test_save_and_load_round_trip(self):
        tracker = StreakTracker()
        tracker.record_completion(date(2027, 1, 1))
        tracker.record_completion(date(2027, 1, 2))
        tracker.record_completion(date(2027, 1, 3))

        self.repository.save(tracker)
        loaded = self.repository.load()

        self.assertEqual(loaded.current_streak, 3)
        self.assertEqual(loaded.longest_streak, 3)
        self.assertEqual(loaded.total_completed_days, 3)
        self.assertEqual(loaded.last_completed_date, date(2027, 1, 3))
        self.assertEqual(len(loaded.history), 3)
        self.assertEqual(loaded.history[0].date, date(2027, 1, 1))

    def test_saving_twice_does_not_duplicate_history(self):
        tracker = StreakTracker()
        tracker.record_completion(date(2027, 1, 1))
        self.repository.save(tracker)
        self.repository.save(tracker)  # save again, unchanged

        loaded = self.repository.load()
        self.assertEqual(len(loaded.history), 1)  # not 2

    def test_load_with_no_saved_streak_returns_fresh_tracker(self):
        loaded = self.repository.load()
        self.assertEqual(loaded.current_streak, 0)
        self.assertEqual(len(loaded.history), 0)


if __name__ == "__main__":
    unittest.main()