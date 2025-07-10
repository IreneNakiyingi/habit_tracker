# habit_tracker/models/habit.py
from datetime import datetime

class Habit:
    def __init__(self, name, periodicity, created_at=None, checkoffs=None):
        self.name = name
        self.periodicity = periodicity
        self.created_at = created_at or datetime.now().isoformat()
        self.checkoffs = checkoffs or []

    def mark_complete(self):
        today = datetime.now().date().isoformat()
        if today not in self.checkoffs:
            self.checkoffs.append(today)

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Habit(data['name'], data['periodicity'], data['created_at'], data['checkoffs'])

    def __str__(self):
        return f"{self.name} ({self.periodicity}) - {len(self.checkoffs)} completions"