import unittest

from system.errors import QuestAlreadyCompletedError
from system.quest import Quest, QuestStatus

class TestNewQuest(unittest.TestCase):
    def setUp(self):
        self.quest = Quest("daily_workout", "Complete a workout", 3)

    def test_starts_not_started(self):
        self.assertEqual(self.quest.status, QuestStatus.NOT_STARTED)
        self.assertFalse(self.quest.is_completed())

    def test_stores_fields_as_given(self):
        self.assertEqual(self.quest.quest_id, "daily_workout")
        self.assertEqual(self.quest.name, "Complete a workout")
        self.assertEqual(self.quest.reward_points, 3)

class TestCompleteQuest(unittest.TestCase):
    def setUp(self):
        self.quest = Quest("daily_workout", "Complete a workout", 3)

    def test_completing_changes_status(self):
        self.quest.complete()
        self.assertEqual(self.quest.status, QuestStatus.COMPLETED)
        self.assertTrue(self.quest.is_completed())

    def test_completing_twice_raises(self):
        self.quest.complete()
        with self.assertRaises(QuestAlreadyCompletedError):
            self.quest.complete()

if __name__ == "__main__":
    unittest.main()