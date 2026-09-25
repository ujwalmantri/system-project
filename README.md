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
- Unit tests for both Player and Quest (11 tests)

Not built yet: quest engine (connecting quest completion to player rewards),
streaks, persistence, loot boxes.

## Setup

    python -m venv .venv
    source .venv/bin/activate

## Roadmap

Domain model first, then persistence, quests, workouts, API, and frontend.