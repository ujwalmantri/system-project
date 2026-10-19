"""
Saves Quest objects in database
"""

from system.quest import Quest

class QuestRepository:
    def __init__(self, connection):
        self.connection = connection

    def save(self, quest):

        self.connection.execute(
            """
            INSERT INTO quests
                (quest_id, name, reward_points, status)
            VALUES (?, ?, ?, ?)
            """,
            (
                quest.quest_id,
                quest.name,
                quest.reward_points,
                quest.status.value
                            
            )
        )
        self.connection.commit()

    def load(self, quest_id):
        cursor = self.connection.execute(
            "SELECT name, reward_points, status "
            "FROM quests WHERE quest_id = ?",
            (quest_id,),
        )
        row = cursor.fetchone()

        name, reward_points, status = row

        quest = Quest(quest_id=quest_id, name=name, reward_points=reward_points)
        if status == "completed":
            quest.complete()
        return quest
