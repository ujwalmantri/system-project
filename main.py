"""SYSTEM: entry point. Run this to interact with your player for today."""

from datetime import date

from system.database import create_tables, get_connection
from system.player import Player
from system.player_repository import PlayerRepository
from system.progression_service import ProgressionService
from system.quest import Quest
from system.quest_service import QuestService
from system.streak_tracker_repository import StreakTrackerRepository


def main():
    connection = get_connection()
    create_tables(connection)

    player_repo = PlayerRepository(connection)
    streak_repo = StreakTrackerRepository(connection)

    player = player_repo.load(player_id=1)
    if player is None:
        player = Player("Hunter")
        player_repo.save(player)
        print(f"Created new player: {player.name}")

    tracker = streak_repo.load(streak_id=1)
    today = date.today()

    quest = Quest("daily_workout", "Complete a workout", reward_points=3)

    already_done_today = tracker.last_completed_date == today

    if already_done_today:
        print("You've already completed today's daily quest.")
    else:
        quest_service = QuestService()
        quest_service.complete_quest(player, quest)

        progression_service = ProgressionService(tracker)
        progression_service.record_daily_completion(player, today)

        print("Daily quest completed! +{} ability points.".format(quest.reward_points))

    player_repo.save(player)
    streak_repo.save(tracker)

    print(f"\n{player.name} — Level {player.level}")
    print(f"Ability points available: {player.ability_points}")
    print(f"Current streak: {tracker.current_streak} (longest: {tracker.longest_streak})")

    connection.close()


if __name__ == "__main__":
    main()