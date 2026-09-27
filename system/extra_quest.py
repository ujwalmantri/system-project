"""
ExtraQuest: an optional, unlimited-completion quest.

Unlike Quest, an ExtraQuest has no 'already completed' state; it can be completed any number of times and never breaks the streak.
"""

from dataclasses import dataclass

@dataclass
class ExtraQuest:
    quest_id: str
    name: str
    reward_points:int

