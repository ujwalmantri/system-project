"""
The Quest Entity: a real-world task the player can complete.
"""

from enum import Enum

from system.errors import QuestAlreadyCompletedError

class QuestStatus(Enum):
    NOT_STARTED = "not_started"
    COMPLETED = "completed"

class Quest:
    def __init__(self, quest_id, name, reward_points):
        self.quest_id = quest_id
        self.name = name
        self.reward_points = reward_points
        self.status = QuestStatus.NOT_STARTED

    def complete(self):
        if self.status == QuestStatus.COMPLETED:
            raise QuestAlreadyCompletedError(f"Quest {self.quest_id!r} is already completed.")
        self.status = QuestStatus.COMPLETED

    def is_completed(self):
        return self.status == QuestStatus.COMPLETED