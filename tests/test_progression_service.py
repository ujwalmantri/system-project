import unittest
from datetime import date

from system.player import Player
from system.progression_service import ProgressionService
from system.streak_tracker import StreakTracker


class TestProgressionService(unittest.TestCase):
    def setUp(self):
        self.player = Player("Hunter")
        self.tracker = StreakTracker()
        self.service = ProgressionService(self.tracker)

    def test_level_stays_one_before_ten_days(self):
        for day in range(1, 10):  # 9 days
            self.service.record_daily_completion(self.player, date(2027, 1, day))
        self.assertEqual(self.player.level, 1)

    def test_level_reaches_two_at_ten_days(self):
        for day in range(1, 11):  # 10 days
            self.service.record_daily_completion(self.player, date(2027, 1, day))
        self.assertEqual(self.player.level, 2)

    def test_level_does_not_regress_after_streak_break(self):
        for day in range(1, 11):  # reach level 2
            self.service.record_daily_completion(self.player, date(2027, 1, day))
        self.service.record_daily_completion(self.player, date(2027, 1, 20))
        self.assertEqual(self.player.level, 2)
        self.assertEqual(self.tracker.current_streak, 1)


if __name__ == "__main__":
    unittest.main()