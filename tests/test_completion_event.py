import unittest
from datetime import date

from system.completion_event import CompletionEvent

class TestCompletionEvent(unittest.TestCase):
    def test_stores_given_values(self):
        event = CompletionEvent(
            date=date(2027, 1, 1),
            streak_at_completion=1,
            total_completed_days_at_completion=1,
        )

        self.assertEqual(event.date, date(2027, 1, 1))
        self.assertEqual(event.streak_at_completion, 1)
        self.assertEqual(event.total_completed_days_at_completion, 1)

    def test_is_immutable(self):
        event = CompletionEvent(
            date=date(2027, 1, 1),
            streak_at_completion=1,
            total_completed_days_at_completion=1,
        )
        with self.assertRaises(Exception):
            event.date = date(2027, 1, 2)

if __name__ == "__main__":
    unittest.main()