"""
Custom errors for the SYSTEM.
"""

class InvalidAmountError(Exception):
    """The amount of points is not a positive whole numbers."""

class InvalidAttributeError(Exception):
    """The thing given is not one of the five attributes."""

class InsufficientPointsError(Exception):
    """The player tried to spend more points than they have."""

class QuestAlreadyCompletedError(Exception):
    """The quest was already completed and can't be completed again"""