# tests/test_analytics.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.habit import Habit
from services.manager import HabitManager
from services.analytics import (
    get_all_habits,
    get_habits_by_periodicity,
    get_longest_streak_all,
    get_longest_streak_for_habit,
    get_most_frequent_habit,
    get_completion_rate,
    get_weekly_average
)
from datetime import datetime, timedelta

def test_get_all_habits():
    manager = HabitManager()
    manager.habits = [
        Habit("Water", "daily"),
        Habit("Run", "weekly")
    ]
    assert get_all_habits(manager) == ["Water", "Run"]

def test_get_habits_by_periodicity():
    manager = HabitManager()
    manager.habits = [
        Habit("Water", "daily"),
        Habit("Run", "weekly"),
        Habit("Sleep", "daily")
    ]
    assert get_habits_by_periodicity(manager, "daily") == ["Water", "Sleep"]

def test_get_longest_streak_for_habit():
    h = Habit("Exercise", "daily", checkoffs=["2025-07-01", "2025-07-02", "2025-07-04"])
    assert get_longest_streak_for_habit(h) == 2

def test_get_longest_streak_all():
    manager = HabitManager()
    h1 = Habit("A", "daily", checkoffs=["2025-07-01", "2025-07-02", "2025-07-04"])
    h2 = Habit("B", "daily", checkoffs=["2025-07-01", "2025-07-02", "2025-07-03"])
    manager.habits = [h1, h2]
    result = get_longest_streak_all(manager)
    assert result == {"A": 2, "B": 3}

def test_get_most_frequent_habit():
    h1 = Habit("A", "daily", checkoffs=["2025-07-01", "2025-07-02"])
    h2 = Habit("B", "daily", checkoffs=["2025-07-01", "2025-07-02", "2025-07-03"])
    manager = HabitManager()
    manager.habits = [h1, h2]
    most = get_most_frequent_habit(manager)
    assert most.name == "B"

def test_get_completion_rate():
    created_at = (datetime.today() - timedelta(days=10)).isoformat()
    h = Habit("Test", "daily", created_at=created_at, checkoffs=["2025-07-01", "2025-07-02", "2025-07-03"])
    rate = get_completion_rate(h)
    assert isinstance(rate, float)
    assert rate >= 0

def test_get_weekly_average():
    created_at = (datetime.today() - timedelta(weeks=2)).isoformat()
    h = Habit("Test", "daily", created_at=created_at, checkoffs=["2025-07-01", "2025-07-02", "2025-07-03"])
    avg = get_weekly_average(h)
    assert isinstance(avg, float)
    assert avg >= 0
