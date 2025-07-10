# habit_tracker/main.py
from services.manager import HabitManager
from services.analytics import (
    get_all_habits, get_habits_by_periodicity,
    get_longest_streak_all, get_longest_streak_for_habit
)

def main():
    manager = HabitManager()
    manager.load_data()

    while True:
        print("\nHabit Tracker")
        print("1. Create Habit")
        print("2. List Habits")
        print("3. Complete Habit")
        print("4. Analytics")
        print("5. Save & Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Habit name: ")
            freq = input("Periodicity (daily/weekly): ")
            manager.create_habit(name, freq)

        elif choice == '2':
            for habit in manager.list_habits():
                print(habit)

        elif choice == '3':
            name = input("Enter habit name: ")
            manager.mark_habit_complete(name)

        elif choice == '4':
            print("\nAll habits:")
            print(get_all_habits(manager))
            print("\nLongest streaks:")
            print(get_longest_streak_all(manager))

        elif choice == '5':
            manager.save_data()
            break

if __name__ == '__main__':
    main()