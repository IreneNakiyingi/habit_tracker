# habit_tracker/services/manager.py
"""
Manages the creation, modification, and persistence of habits.

Provides CRUD functionality and data loading/saving to JSON files.
"""

import os
import json
from models.habit import Habit

class HabitManager:
    """
    Central class for managing all user habits.

    Attributes:
        habits (list): A list of Habit instances.
        data_path (str): File path for storing user habit data.
        example_path (str): File path for loading predefined habits.
    """
    def __init__(self):
        self.habits = []
        self.data_path = 'data/habits_data.json'
        self.example_path = 'fixtures/example_data.json'

    def load_data(self, path):
        """Loads habits from a specified JSON file."""
        if os.path.exists(path):
            with open(path, 'r') as f:
                data = json.load(f)
                self.habits = [Habit.from_dict(h) for h in data]

    def save_data(self):
        """Saves the current habit list to the data file."""
        with open(self.data_path, 'w') as f:
            json.dump([h.to_dict() for h in self.habits], f, indent=2)

    def load_or_initialize(self):
        """Loads user data or initializes with example data if none exists."""
        if os.path.exists(self.data_path):
            self.load_data(self.data_path)
        else:
            self.load_data(self.example_path)
            self.save_data()

    def create_habit(self, name, periodicity):
        """Creates a new habit and saves the state."""
        self.habits.append(Habit(name, periodicity))
        self.save_data()

    def update_habit(self, old_name, new_name=None, new_periodicity=None):
        """Updates an existing habit's name and/or periodicity."""
        for habit in self.habits:
            if habit.name == old_name:
                if new_name:
                    habit.name = new_name
                if new_periodicity:
                    habit.periodicity = new_periodicity
                self.save_data()
                break

    def delete_habit(self, name):
        """Deletes a habit by name."""
        self.habits = [h for h in self.habits if h.name != name]
        self.save_data()

    def list_habits(self):
        """Returns the list of all current habits."""
        return self.habits

    def mark_habit_complete(self, name):
        """Marks a habit as completed for the current date."""
        for habit in self.habits:
            if habit.name == name:
                habit.mark_complete()
                self.save_data()
                break
