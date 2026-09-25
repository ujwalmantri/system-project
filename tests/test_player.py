import unittest

from system.attribute import Attribute
from system.errors import (
    InsufficientPointsError,
    InvalidAmountError,
    InvalidAttributeError,
)
from system.player import Player

class TestNewPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player("Hunter")

    def test_starts_at_level_one_with_no_points(self):
        self.assertEqual(self.player.level, 1)
        self.assertEqual(self.player.ability_points, 0)

    def test_every_attribute_starts_at_ten(self):
        for attribute in Attribute:
            self.assertEqual(self.player.attributes[attribute], 10)

class TestAddAbilityPoints(unittest.TestCase):
    def setUp(self):
        self.player = Player("Hunter")

    def test_adding_points_increases_balance(self):
        self.player.add_ability_points(3)
        self.assertEqual(self.player.ability_points, 3)

    def test_rejects_invalid_amounts(self):
        for bad in (0, -1, 1.5, True):
            with self.assertRaises(InvalidAmountError):
                self.player.add_ability_points(bad)

class TestAllocatePoints(unittest.TestCase):
    def setUp(self):
        self.player = Player("Hunter")
        self.player.add_ability_points(3)

    def test_valid_allocation_moves_points(self):
        self.player.allocate_points(Attribute.STRENGTH, 2)
        self.assertEqual(self.player.attributes[Attribute.STRENGTH], 12)
        self.assertEqual(self.player.ability_points, 1)

    def test_insufficient_points_rejected(self):
        with self.assertRaises(InsufficientPointsError):
            self.player.allocate_points(Attribute.STRENGTH, 4)

        self.assertEqual(self.player.ability_points, 3)

    def test_invalid_attribute_rejected(self):
        with self.assertRaises(InvalidAttributeError):
            self.player.allocate_points("strength",1)

if __name__ == "__main__":
    unittest.main()