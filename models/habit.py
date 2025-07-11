# habit_tracker/models/habit.py
"""
Defines the Habit class used in the Habit Tracker application.

Each Habit instance holds information about the task name, periodicity,
creation date, and check-off history.
"""

from datetime import datetime

class Habit:
    """
    Represents a user-defined habit.

    Attributes:
        name (str): The name of the habit.
        periodicity (str): Either 'daily' or 'weekly'.
        created_at (str): Timestamp of when the habit was created.
        checkoffs (list): Dates when the habit was completed.
    """
    def __init__(self, name, periodicity, created_at=None, checkoffs=None):
        """
        Initializes a new Habit object.

        Args:
            name (str): The name of the habit.
            periodicity (str): Frequency of the habit (daily/weekly).
            created_at (str, optional): ISO timestamp. Defaults to now.
            checkoffs (list, optional): List of completion dates.
        """
        self.name = name
        self.periodicity = periodicity
        self.created_at = created_at or datetime.now().isoformat()
        self.checkoffs = checkoffs or []

    def mark_complete(self):
        """Marks the habit as completed for the current day."""
        today = datetime.now().date().isoformat()
        if today not in self.checkoffs:
            self.checkoffs.append(today)

    def to_dict(self):
        """Serializes the habit object to a dictionary."""
        return self.__dict__

    @staticmethod
    def from_dict(data):
        """Creates a Habit object from a dictionary."""
        return Habit(data['name'], data['periodicity'], data['created_at'], data['checkoffs'])

    def __str__(self):
        """String representation of a habit."""
        return f"{self.name} ({self.periodicity}) - {len(self.checkoffs)} completions"