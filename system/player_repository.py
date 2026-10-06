"""
Saves and loads Player objects from database
"""

from system.attribute import Attribute
from system.player import Player

class PlayerRepository:
    def __init__(self, connection):
        self.connection = connection

    def save(self, player):
        attrs = player.attributes
        self.connection.execute(
            """
            INSERT INTO players
                (name, level, ability_points, strength, agility, vitality, intelligence, perception)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                player.name,
                player.level,
                player.ability_points,
                attrs[Attribute.STRENGTH],
                attrs[Attribute.AGILITY],
                attrs[Attribute.VITALITY],
                attrs[Attribute.INTELLIGENCE],
                attrs[Attribute.PERCEPTION],
            ),
        )
        self.connection.commit()

    def load(self, player_id):
        cursor = self.connection.execute(
            "SELECT name, level, ability_points, strength, agility, vitality, intelligence, perception "
            "FROM players WHERE id = ?",
            (player_id,),
        )
        row = cursor.fetchone()

        name, level, ability_points, strength, agility, vitality, intelligence, perception = row

        player = Player(name)
        player.set_level(level)
        player.add_ability_points(ability_points)
        player.attributes[Attribute.STRENGTH] = strength
        player.attributes[Attribute.AGILITY] = agility
        player.attributes[Attribute.VITALITY] = vitality
        player.attributes[Attribute.INTELLIGENCE] = intelligence
        player.attributes[Attribute.PERCEPTION] = perception
        return player