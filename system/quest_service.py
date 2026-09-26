"""
Connects quest completion to player rewards
"""

class QuestService:
    def complete_quest(self, player, quest):
        quest.complete()
        player.add_ability_points(quest.reward_points)