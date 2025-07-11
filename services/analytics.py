# habit_tracker/services/analytics.py
"""
Functional module for analyzing habit data.

Includes functions to compute streaks, frequency, and habit performance.
All functions are stateless and operate on passed data only.
"""

from datetime import datetime;

# Pure functional style helpers
def get_all_habits(manager):
    """Returns a list of habit names from the manager."""
    return [h.name for h in manager.habits]

def get_habits_by_periodicity(manager, periodicity):
    """Returns names of habits that match a given periodicity."""
    return [h.name for h in manager.habits if h.periodicity == periodicity]

def get_longest_streak_all(manager):
    """Returns a dictionary of longest streaks per habit."""
    return {h.name: get_longest_streak_for_habit(h) for h in manager.habits}

def get_longest_streak_for_habit(habit):
    """
    Calculates the longest streak of consecutive completions.

    Args:
        habit (Habit): A habit object.

    Returns:
        int: Maximum number of consecutive days.
    """
    dates = sorted(datetime.fromisoformat(d).date() for d in habit.checkoffs)
    if not dates:
        return 0
    streak = max_streak = 1
    for i in range(1, len(dates)):
        delta = (dates[i] - dates[i - 1]).days
        if delta == 1:
            streak += 1
        else:
            max_streak = max(max_streak, streak)
            streak = 1
    return max(max_streak, streak)

def get_most_frequent_habit(manager):
    """Returns the habit with the highest number of check-offs."""
    return max(manager.habits, key=lambda h: len(h.checkoffs), default=None)

def get_completion_rate(habit):
    """
    Calculates the percentage of days the habit was completed.

    Args:
        habit (Habit): The habit instance.

    Returns:
        float: Completion rate in percent.
    """
    from datetime import datetime, timedelta
    if not habit.checkoffs:
        return 0
    start = datetime.fromisoformat(habit.created_at).date()
    today = datetime.today().date()
    days = (today - start).days or 1
    return round(len(habit.checkoffs) / days * 100, 2)

def get_weekly_average(habit):
    """
    Calculates the average number of completions per week.

    Args:
        habit (Habit): The habit instance.

    Returns:
        float: Completions per week.
    """
    from datetime import datetime
    if not habit.checkoffs:
        return 0
    days = (datetime.today().date() - datetime.fromisoformat(habit.created_at).date()).days or 1
    weeks = days / 7
    return round(len(habit.checkoffs) / weeks, 2)
