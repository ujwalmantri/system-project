"""
A permanent record of one completed day.

Once created, a CompletionEvent never changes, it's a fact about something that alredy happened.
"""

from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class CompletionEvent:
    date: date
    streak_at_completion: int
    total_completed_days_at_completion: int
    