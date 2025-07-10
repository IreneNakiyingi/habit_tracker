# habit_tracker/services/analytics.py
from datetime import datetime;

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

def get_most_frequent_habit(manager):
    return max(manager.habits, key=lambda h: len(h.checkoffs), default=None)

def get_completion_rate(habit):
    from datetime import datetime, timedelta
    if not habit.checkoffs:
        return 0
    start = datetime.fromisoformat(habit.created_at).date()
    today = datetime.today().date()
    days = (today - start).days or 1
    return round(len(habit.checkoffs) / days * 100, 2)
def get_weekly_average(habit):
    from datetime import datetime
    if not habit.checkoffs:
        return 0
    days = (datetime.today().date() - datetime.fromisoformat(habit.created_at).date()).days or 1
    weeks = days / 7
    return round(len(habit.checkoffs) / weeks, 2)
