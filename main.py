# habit_tracker/main.py
"""
Main entry point for the Habit Tracker CLI application.

Provides a command-line interface to manage habits:
creating, listing, editing, deleting, completing, and analyzing habits.
"""

from services.manager import HabitManager
from services.analytics import (
    get_all_habits, get_habits_by_periodicity,
    get_longest_streak_all, get_longest_streak_for_habit,
    get_most_frequent_habit, get_completion_rate, get_weekly_average
)

def display_habits(habits):
    """Prints a formatted list of habits."""
    print("\nYour Habits:")
    print("=" * 50)
    for h in habits:
        print(f"Name: {h.name}\tPeriodicity: {h.periodicity}\tCompletions: {len(h.checkoffs)}")
    print("=" * 50)

def main():
    """Runs the interactive command-line loop for the habit tracker."""
    manager = HabitManager()
    manager.load_or_initialize()

    while True:
        print("\nHabit Tracker")
        print("1. Create Habit")
        print("2. List Habits")
        print("3. Complete Habit")
        print("4. Edit Habit")
        print("5. Delete Habit")
        print("6. Analytics")
        print("7. Save & Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Habit name: ")
            freq = input("Periodicity (daily/weekly): ")
            manager.create_habit(name, freq)

        elif choice == '2':
            display_habits(manager.list_habits())

        elif choice == '3':
            name = input("Enter habit name to complete: ")
            manager.mark_habit_complete(name)

        elif choice == '4':
            old_name = input("Enter current habit name: ")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_freq = input("Enter new periodicity (leave blank to keep current): ")
            manager.update_habit(old_name, new_name or None, new_freq or None)

        elif choice == '5':
            name = input("Enter habit name to delete: ")
            confirm = input(f"Are you sure you want to delete '{name}'? (y/n): ")
            if confirm.lower() == 'y':
                manager.delete_habit(name)

        elif choice == '6':
            print("\nAnalytics Report")
            streaks = get_longest_streak_all(manager)
            for name, days in streaks.items():
                print(f"- {name}: Longest streak = {days} days")

            frequent = get_most_frequent_habit(manager)
            if frequent:
                print(f"\nMost Frequent Habit: {frequent.name} ({len(frequent.checkoffs)} completions)")
                print(f"Completion Rate: {get_completion_rate(frequent)}%")
                print(f"Weekly Average: {get_weekly_average(frequent)} times/week")

        elif choice == '7':
            manager.save_data()
            break

if __name__ == '__main__':
    main()
