"""The Player entity: the character whose progress the SYSTEM tracks."""

from system.attribute import Attribute
from system.errors import (
    InsufficientPointsError,
    InvalidAmountError,
    InvalidAttributeError,
)

STARTING_LEVEL = 1
STARTING_ATTRIBUTE_VALUE = 10


class Player:
    def __init__(self, name):
        self.name = name
        self._level = STARTING_LEVEL
        self._ability_points = 0
        self._attributes = {}
        for attribute in Attribute:
            self._attributes[attribute] = STARTING_ATTRIBUTE_VALUE

    # ---- level ----

    @property
    def level(self):
        return self._level

    def set_level(self, level):
        if isinstance(level, bool) or not isinstance(level, int) or level < 1:
            raise InvalidAmountError(f"{level!r} is not a valid level.")
        self._level = level

    # ---- ability points ----

    @property
    def ability_points(self):
        return self._ability_points

    def add_ability_points(self, amount):
        self._check_amount(amount)
        self._ability_points += amount

    def set_ability_points(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, int) or amount < 0:
            raise InvalidAmountError(f"{amount!r} is not a valid ability point total.")
        self._ability_points = amount

    # ---- attributes ----

    @property
    def attributes(self):
        return dict(self._attributes)

    def set_attribute(self, attribute, value):
        if not isinstance(attribute, Attribute):
            raise InvalidAttributeError(f"{attribute!r} is not a valid attribute.")
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise InvalidAmountError(f"{value!r} is not a valid attribute value.")
        self._attributes[attribute] = value

    def allocate_points(self, attribute, amount):
        # 1. Validate everything first...
        if not isinstance(attribute, Attribute):
            raise InvalidAttributeError(f"{attribute!r} is not a valid attribute.")
        self._check_amount(amount)
        if amount > self._ability_points:
            raise InsufficientPointsError(
                f"Tried to spend {amount}, but only {self._ability_points} available."
            )
        # 2. ...and only then change state.
        self._ability_points -= amount
        self.set_attribute(attribute, self._attributes[attribute] + amount)

    def get_attribute(self, attribute):
        if not isinstance(attribute, Attribute):
            raise InvalidAttributeError(f"{attribute!r} is not a valid attribute.")
        return self._attributes[attribute]

    # ---- internal ----

    def _check_amount(self, amount):
        if isinstance(amount, bool) or not isinstance(amount, int) or amount <= 0:
            raise InvalidAmountError(f"{amount!r} is not a positive whole number.")