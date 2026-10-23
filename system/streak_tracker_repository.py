"""Saves and loads StreakTracker objects from the database."""

from datetime import date as date_cls

from system.completion_event import CompletionEvent
from system.streak_tracker import StreakTracker


class StreakTrackerRepository:
    def __init__(self, connection):
        self.connection = connection

    def save(self, tracker, streak_id=1):
        last_date_str = (
            tracker.last_completed_date.isoformat()
            if tracker.last_completed_date is not None
            else None
        )

        existing = self.connection.execute(
            "SELECT id FROM streaks WHERE id = ?", (streak_id,)
        ).fetchone()

        if existing is None:
            self.connection.execute(
                """
                INSERT INTO streaks
                    (id, current_streak, longest_streak, total_completed_days, last_completed_date)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    streak_id,
                    tracker.current_streak,
                    tracker.longest_streak,
                    tracker.total_completed_days,
                    last_date_str,
                ),
            )
        else:
            self.connection.execute(
                """
                UPDATE streaks
                SET current_streak = ?, longest_streak = ?, total_completed_days = ?, last_completed_date = ?
                WHERE id = ?
                """,
                (
                    tracker.current_streak,
                    tracker.longest_streak,
                    tracker.total_completed_days,
                    last_date_str,
                    streak_id,
                ),
            )

        # Delete-then-reinsert: the simple, correct way to keep history in sync.
        self.connection.execute(
            "DELETE FROM completion_events WHERE streak_id = ?", (streak_id,)
        )
        for event in tracker.history:
            self.connection.execute(
                """
                INSERT INTO completion_events
                    (streak_id, date, streak_at_completion, total_completed_days_at_completion)
                VALUES (?, ?, ?, ?)
                """,
                (
                    streak_id,
                    event.date.isoformat(),
                    event.streak_at_completion,
                    event.total_completed_days_at_completion,
                ),
            )

        self.connection.commit()

    def load(self, streak_id=1):
        row = self.connection.execute(
            "SELECT current_streak, longest_streak, total_completed_days, last_completed_date "
            "FROM streaks WHERE id = ?",
            (streak_id,),
        ).fetchone()

        tracker = StreakTracker()
        if row is None:
            return tracker  # no saved streak yet, return a fresh one

        current_streak, longest_streak, total_completed_days, last_date_str = row
        tracker.current_streak = current_streak
        tracker.longest_streak = longest_streak
        tracker.total_completed_days = total_completed_days
        tracker.last_completed_date = (
            date_cls.fromisoformat(last_date_str) if last_date_str is not None else None
        )

        event_rows = self.connection.execute(
            "SELECT date, streak_at_completion, total_completed_days_at_completion "
            "FROM completion_events WHERE streak_id = ? ORDER BY id",
            (streak_id,),
        ).fetchall()

        for event_date_str, streak_at, total_at in event_rows:
            tracker.history.append(
                CompletionEvent(
                    date=date_cls.fromisoformat(event_date_str),
                    streak_at_completion=streak_at,
                    total_completed_days_at_completion=total_at,
                )
            )
        return tracker