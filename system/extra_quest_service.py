"""
Completing an ExtraQuest: unlimited, always grants a small record.
"""

class ExtraQuestService:
    def complete_extra_quest(self, player, extra_quest, confirmed):
        if not confirmed:
            return "System requires confirmation before granting this reward"
        player.add_ability_points(extra_quest.reward_points)
        return f"System acknowledges: you completed {extra_quest.name!r}."