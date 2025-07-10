# tests/test.py
#import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.habit import Habit
from services.manager import HabitManager
from services.analytics import get_longest_streak_for_habit

def test_habit_creation():
    h = Habit("Test", "daily")
    assert h.name == "Test"
    assert h.periodicity == "daily"
    assert isinstance(h.created_at, str)
    assert h.checkoffs == []

def test_mark_complete_adds_today():
    h = Habit("Test", "daily")
    h.mark_complete()
    assert len(h.checkoffs) == 1
    assert h.checkoffs[0] == h.checkoffs[-1]

def test_duplicate_completion_not_added():
    h = Habit("Test", "daily")
    h.mark_complete()
    h.mark_complete()  # second call shouldn't duplicate
    assert len(h.checkoffs) == 1

def test_longest_streak():
    h = Habit("Test", "daily", checkoffs=["2025-07-01", "2025-07-02", "2025-07-04"])
    assert get_longest_streak_for_habit(h) == 2

def test_manager_create_and_list():
    manager = HabitManager()
    manager.habits = []  # Reset state for test
    manager.create_habit("Test", "daily")
    assert len(manager.list_habits()) == 1
    assert manager.list_habits()[0].name == "Test"

def test_manager_mark_complete():
    manager = HabitManager()
    manager.habits = []
    manager.create_habit("Test", "daily")
    manager.mark_habit_complete("Test")
    assert len(manager.list_habits()[0].checkoffs) == 1

def test_manager_delete_habit():
    manager = HabitManager()
    manager.habits = []
    manager.create_habit("Test", "daily")
    manager.delete_habit("Test")
    assert len(manager.habits) == 0

def test_manager_update_habit():
    manager = HabitManager()
    manager.habits = []
    manager.create_habit("OldName", "daily")
    manager.update_habit("OldName", new_name="NewName", new_periodicity="weekly")
    updated = manager.list_habits()[0]
    assert updated.name == "NewName"
    assert updated.periodicity == "weekly"
