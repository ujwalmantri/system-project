import unittest
from datetime import date 
from system.streak_tracker import StreakTracker

class TestStreakTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = StreakTracker()

    def test_first_completion_starts_streak_at_one(self):
        self.tracker.record_completion(date(2027, 1, 1))
        self.assertEqual(self.tracker.current_streak, 1)
        self.assertEqual(self.tracker.total_completed_days, 1)

    def test_same_day_completion_does_not_change_streak(self):
        self.tracker.record_completion(date(2027, 1, 1))
        self.tracker.record_completion(date(2027, 1, 1))
        self.assertEqual(self.tracker.current_streak, 1)
        self.assertEqual(self.tracker.total_completed_days, 1)

    def test_consecutive_day_increases_streak(self):
        self.tracker.record_completion(date(2027, 1, 1))
        self.tracker.record_completion(date(2027, 1, 2))
        self.assertEqual(self.tracker.current_streak, 2)
        self.assertEqual(self.tracker.total_completed_days, 2)

    def test_missed_day_resets_streak_to_one(self):
        self.tracker.record_completion(date(2027, 1, 1))
        self.tracker.record_completion(date(2027, 1, 2))
        self.tracker.record_completion(date(2027, 1, 4))
        self.assertEqual(self.tracker.current_streak, 1)
        self.assertEqual(self.tracker.total_completed_days, 3)

    def test_longest_streak_survives_a_reset(self):
        self.tracker.record_completion(date(2027, 1, 1))
        self.tracker.record_completion(date(2027, 1, 2))
        self.tracker.record_completion(date(2027, 1, 4))
        self.assertEqual(self.tracker.current_streak, 1)
        self.assertEqual(self.tracker.longest_streak, 2)

if __name__ == "__main__":
    unittest.main()