"""
Tracks daily-completion streaks and total completed days.
"""

from system.completion_event import CompletionEvent
from datetime import timedelta

class StreakTracker:
    def __init__(self):
        self.current_streak = 0
        self.longest_streak = 0
        self.total_completed_days = 0
        self.last_completed_date = None
        self.history = []

    def record_completion(self, date):
        if self.last_completed_date is None:
            self.current_streak = 1
        elif date == self.last_completed_date:
            return
        elif date == self.last_completed_date + timedelta(days=1):
            self.current_streak +=1
        else:
            self.current_streak = 1

        self.total_completed_days += 1
        self.longest_streak = max(self.longest_streak, self.current_streak)
        self.last_completed_date = date
        self.history.append(
            CompletionEvent(
                date=date,
                streak_at_completion=self.current_streak,
                total_completed_days_at_completion=self.total_completed_days,
            )
        )