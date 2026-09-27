import unittest

from system.extra_quest import ExtraQuest
from system.extra_quest_service import ExtraQuestService
from system.player import Player


class TestExtraQuestService(unittest.TestCase):
    def setUp(self):
        self.player = Player("Hunter")
        self.extra_quest = ExtraQuest("extra_pullups", "100 Pull-ups", 1)
        self.service = ExtraQuestService()

    def test_unconfirmed_completion_grants_nothing(self):
        self.service.complete_extra_quest(self.player, self.extra_quest, confirmed=False)
        self.assertEqual(self.player.ability_points, 0)

    def test_confirmed_completion_grants_reward(self):
        self.service.complete_extra_quest(self.player, self.extra_quest, confirmed=True)
        self.assertEqual(self.player.ability_points, 1)

    def test_can_be_completed_unlimited_times(self):
        for _ in range(5):
            self.service.complete_extra_quest(self.player, self.extra_quest, confirmed=True)
        self.assertEqual(self.player.ability_points, 5)


if __name__ == "__main__":
    unittest.main()