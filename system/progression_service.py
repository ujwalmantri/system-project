"""
Connects daily completion to streaks and level progression.
"""

class ProgressionService:
    def __init__(self, streak_tracker):
        self.streak_tracker = streak_tracker

    def record_daily_completion(self, player, date):
        self.streak_tracker.record_completion(date)
        new_level = 1 + (self.streak_tracker.total_completed_days // 10 )
        player.set_level(new_level)
