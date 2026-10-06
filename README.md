# SYSTEM

A gamified personal progression engine inspired by the "System" from Solo Leveling.
Real-world activities become RPG-style progression.

The five attributes (Strength, Agility, Vitality, Intelligence, Perception) are
game mechanics, not scientific measurements of anyone's body or mind.

## Status

Early development. Currently working:
- Player with level, ability points, and five attributes
- Adding ability points (validated)
- Allocating points to an attribute (validated)
- Quest with id, name, reward points, and status (not started / completed)
- Completing a quest, guarded against double-completion
- QuestService: connects quest completion to player rewards
- StreakTracker: tracks daily completions, consecutive streaks, missed days,
  and keeps a permanent, immutable history of completion events
- ProgressionService: levels up the player every 10 total completed days
  (levels don't regress if a streak breaks)
- ExtraQuest: unlimited-completion optional quest (dataclass, no status)
- ExtraQuestService: grants a small reward per completion, gated by a
  `confirmed` flag (self-accountability, does not affect streak)
- SQLite persistence for Player (save/load) via PlayerRepository
- Unit tests for all of the above (28 tests)

Not built yet: persistence for Quest/StreakTracker/history, loot boxes, quest verification for daily_workout, attribute guard (tracked as a known gap, see code comments).

## Setup

    python -m venv .venv
    source .venv/bin/activate

## Roadmap

Domain model first, then persistence, quests, workouts, API, and frontend.