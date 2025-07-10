# habit_tracker/services/manager.py
import os
import json
from models.habit import Habit

class HabitManager:
    def __init__(self):
        self.habits = []
        self.data_path = 'data/habits.json'

    def load_data(self, path='data/habits.json'):
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = json.load(f)
                self.habits = [Habit.from_dict(h) for h in data]

    def save_data(self, path='data/habits.json'):
        with open(path, 'w') as f:
            json.dump([h.to_dict() for h in self.habits], f, indent=2)

    def create_habit(self, name, periodicity):
        self.habits.append(Habit(name, periodicity))
        self.save_data()

    def list_habits(self):
        return self.habits

    def mark_habit_complete(self, name):
        for habit in self.habits:
            if habit.name == name:
                habit.mark_complete()
                self.save_data()
                break

    def load_or_initialize(self):
        if os.path.exists(self.data_path):
            self.load_data(self.data_path)
        else:
            self.load_data(self.example_path)
            self.save_data()

    def delete_habit(self, name):
        self.habits = [h for h in self.habits if h.name != name]
        self.save_data()

    def update_habit(self, old_name, new_name=None, new_periodicity=None):
        for habit in self.habits:
            if habit.name == old_name:
                if new_name:
                    habit.name = new_name
                if new_periodicity:
                    habit.periodicity = new_periodicity
                self.save_data()
                break

