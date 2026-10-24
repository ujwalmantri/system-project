import os
import sqlite3
import unittest

from system.attribute import Attribute
from system.player import Player
from system.database import create_tables
from system.player_repository import PlayerRepository

TEST_DB_PATH = "test_system.db"

class TestPlayerRepository(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(TEST_DB_PATH)
        create_tables(self.connection)
        self.repository = PlayerRepository(self.connection)

    def tearDown(self):
        self.connection.close()
        os.remove(TEST_DB_PATH)

    def test_save_and_load_round_trip(self):
        player = Player("Hunter")
        player.add_ability_points(3)
        player.allocate_points(Attribute.STRENGTH, 2)

        self.repository.save(player)
        loaded = self.repository.load(player_id=1)

        self.assertEqual(loaded.name, "Hunter")
        self.assertEqual(loaded.ability_points, 1)
        self.assertEqual(loaded.attributes[Attribute.STRENGTH], 12)


    def test_saving_twice_updates_rather_than_duplicates(self):
        player = Player("Hunter")
        self.repository.save(player)

        player.add_ability_points(5)
        self.repository.save(player)  # save again, should UPDATE not INSERT

        row_count = self.connection.execute(
            "SELECT COUNT(*) FROM players"
        ).fetchone()[0]
        self.assertEqual(row_count, 1)

        loaded = self.repository.load(player_id=1)
        self.assertEqual(loaded.ability_points, 5)

if __name__ == "__main__":
    unittest.main()