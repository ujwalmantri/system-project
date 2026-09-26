import unittest

from system.errors import QuestAlreadyCompletedError
from system.player import Player
from system.quest import Quest
from system.quest_service import QuestService

class TestCompleteQuest(unittest.TestCase):
    def setUp(self):
        self.player = Player("Hunter")
        self.quest = Quest("daily_workout", "Complete a workout", 3)
        self.service = QuestService()

    def test_completing_quest_grants_reward(self):
        self.service.complete_quest(self.player, self.quest)
        self.assertTrue(self.quest.is_completed())
        self.assertEqual(self.player.ability_points, 3)

    def test_completing_twice_raises_and_grants_reward_once(self):
        self.service.complete_quest(self.player, self.quest)
        with self.assertRaises(QuestAlreadyCompletedError):
            self.service.complete_quest(self.player, self.quest)
        self.assertEqual(self.player.ability_points, 3)

if __name__ == "__main__":
    unittest.main()