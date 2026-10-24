"""Saves and loads Player objects from the database."""

from system.attribute import Attribute
from system.player import Player


class PlayerRepository:
    def __init__(self, connection):
        self.connection = connection

    def save(self, player, player_id=1):
        attrs = player.attributes
        existing = self.connection.execute(
            "SELECT id FROM players WHERE id = ?", (player_id,)
        ).fetchone()

        if existing is None:
            self.connection.execute(
                """
                INSERT INTO players
                    (id, name, level, ability_points, strength, agility, vitality, intelligence, perception)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    player_id,
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
        else:
            self.connection.execute(
                """
                UPDATE players
                SET name = ?, level = ?, ability_points = ?, strength = ?, agility = ?, vitality = ?, intelligence = ?, perception = ?
                WHERE id = ?
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
                    player_id,
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
        if row is None:
            return None

        name, level, ability_points, strength, agility, vitality, intelligence, perception = row

        player = Player(name)
        player.set_level(level)
        player.set_ability_points(ability_points)
        player.set_attribute(Attribute.STRENGTH, strength)
        player.set_attribute(Attribute.AGILITY, agility)
        player.set_attribute(Attribute.VITALITY, vitality)
        player.set_attribute(Attribute.INTELLIGENCE, intelligence)
        player.set_attribute(Attribute.PERCEPTION, perception)
        return player