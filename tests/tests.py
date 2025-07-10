# habit_tracker/tests/test_all.py
import pytest
from models.habit import Habit
from services.manager import HabitManager
from services.analytics import get_longest_streak_for_habit

def test_habit_creation():
    h = Habit("Test", "daily")
    assert h.name == "Test"
    assert h.periodicity == "daily"

def test_mark_complete():
    h = Habit("Test", "daily")
    h.mark_complete()
    assert len(h.checkoffs) == 1

def test_longest_streak():
    h = Habit("Test", "daily", checkoffs=["2025-07-01", "2025-07-02", "2025-07-04"])
    assert get_longest_streak_for_habit(h) == 2


def test_manager_crud():
    manager = HabitManager()
    manager.create_habit("Test", "daily")
    assert len(manager.list_habits()) == 1
    manager.mark_habit_complete("Test")
    assert len(manager.list_habits()[0].checkoffs) == 1