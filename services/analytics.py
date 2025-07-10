# habit_tracker/services/analytics.py
from datetime import datetime, timedelta

# Pure functional style helpers
def get_all_habits(manager):
    return [h.name for h in manager.habits]

def get_habits_by_periodicity(manager, periodicity):
    return [h.name for h in manager.habits if h.periodicity == periodicity]

def get_longest_streak_all(manager):
    return {h.name: get_longest_streak_for_habit(h) for h in manager.habits}

def get_longest_streak_for_habit(habit):
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