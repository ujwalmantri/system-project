"""
The player entity: the character whose progress the SYSTEM tracks.
"""

from system.attribute import Attribute
from system.errors import (
    InvalidAmountError, 
    InvalidAttributeError,
    InsufficientPointsError,
)

STARTING_LEVEL = 1
STARTING_ATTRIBUTE_VALUE = 10

class Player:
    def __init__(self, name):
        self.name = name
        self._level = STARTING_LEVEL
        self._ability_points = 0
        self.attributes = {}
        for attribute in Attribute:
            self.attributes[attribute] = STARTING_ATTRIBUTE_VALUE

    def _check_amount(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, int) or amount <= 0:
            raise InvalidAmountError(f"{amount!r} is not a positive whole number.")

    def add_ability_points(self, amount):
        self._check_amount(amount)
        self._ability_points += amount

    def allocate_points(self, attribute, amount):
        # check if attribue selected is among the given 5 attributes
        if not isinstance(attribute, Attribute):
            raise InvalidAttributeError(f"{attribute!r} is not a valid attribute.")

        # check if amount is a whole number
        self._check_amount(amount)

        # check if user has enough points to spend
        if amount > self._ability_points:
            raise InsufficientPointsError(f"Tried to spend {amount}, but only {self._ability_points} available.")

        self._ability_points -= amount
        self.attributes[attribute] += amount
        

    @property
    def ability_points(self):
        return self._ability_points    

    @property
    def level(self):
        return self._level

    def set_level(self, level):
        if isinstance(level, bool) or not isinstance(level, int) or level < 1:
            raise InvalidAmountError(f"{level!r} is not a valid level.")
        self._level = level