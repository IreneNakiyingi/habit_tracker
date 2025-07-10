# habit_tracker/services/manager.py
import os
import json
from models.habit import Habit

class HabitManager:
    def __init__(self):
        self.habits = []

    def load_data(self, path='data/habits_data.json'):
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = json.load(f)
                self.habits = [Habit.from_dict(h) for h in data]

    def save_data(self, path='data/habits_data.json'):
        with open(path, 'w') as f:
            json.dump([h.to_dict() for h in self.habits], f, indent=2)

    def create_habit(self, name, periodicity):
        self.habits.append(Habit(name, periodicity))

    def list_habits(self):
        return self.habits

    def mark_habit_complete(self, name):
        for habit in self.habits:
            if habit.name == name:
                habit.mark_complete()
                break