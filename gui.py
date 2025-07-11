# habit_tracker/gui.py
"""
GUI module for the Habit Tracker App using Tkinter.

Provides an interactive graphical interface for creating, editing,
deleting, and completing habits, as well as viewing analytics.
Built with Python's Tkinter library.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog
from services.manager import HabitManager
from services.analytics import (
    get_longest_streak_all,
    get_completion_rate,
    get_most_frequent_habit,
    get_weekly_average
)

class HabitApp:
    """
    Main GUI application class for the Habit Tracker.

    Attributes:
        root (Tk): The main window of the Tkinter application.
        manager (HabitManager): Handles habit operations and data.
        habit_listbox (Listbox): Displays the list of habits.
    """

    def __init__(self, root):
        """Initializes the GUI, widgets, and loads saved or example data."""
        self.root = root
        self.root.title("Habit Tracker")
        self.manager = HabitManager()
        self.manager.load_or_initialize()

        self.habit_listbox = tk.Listbox(root, width=50)
        self.habit_listbox.pack(pady=10)

        self.refresh_habit_list()

        tk.Button(root, text="Create Habit", command=self.create_habit).pack(fill="x")
        tk.Button(root, text="Edit Habit", command=self.edit_habit).pack(fill="x")
        tk.Button(root, text="Delete Habit", command=self.delete_habit).pack(fill="x")
        tk.Button(root, text="Complete Habit", command=self.complete_habit).pack(fill="x")
        tk.Button(root, text="List Habits", command=self.refresh_habit_list).pack(fill="x")
        tk.Button(root, text="Show Analytics", command=self.show_analytics).pack(fill="x")
        tk.Button(root, text="Save & Quit", command=self.quit_app).pack(fill="x")

    def refresh_habit_list(self):
        """Refreshes the displayed list of habits in the GUI."""
        self.habit_listbox.delete(0, tk.END)
        for habit in self.manager.list_habits():
            self.habit_listbox.insert(tk.END, str(habit))

    def create_habit(self):
        """Prompts user to enter and create a new habit."""
        name = simpledialog.askstring("Habit Name", "Enter habit name:")
        periodicity = simpledialog.askstring("Periodicity", "Enter periodicity (daily/weekly):")
        if name and periodicity:
            self.manager.create_habit(name, periodicity)
            self.refresh_habit_list()

    def edit_habit(self):
        """Allows user to edit the selected habit's name and periodicity."""
        selection = self.habit_listbox.curselection()
        if selection:
            old_name = self.habit_listbox.get(selection[0]).split(" (")[0]
            new_name = simpledialog.askstring("New Name", "Enter new name:")
            new_periodicity = simpledialog.askstring("New Periodicity", "Enter new periodicity:")
            self.manager.update_habit(old_name, new_name, new_periodicity)
            self.refresh_habit_list()

    def delete_habit(self):
        """Deletes the selected habit after user confirmation."""
        selection = self.habit_listbox.curselection()
        if selection:
            habit_name = self.habit_listbox.get(selection[0]).split(" (")[0]
            confirm = messagebox.askyesno("Delete Habit", f"Are you sure you want to delete '{habit_name}'?")
            if confirm:
                self.manager.delete_habit(habit_name)
                self.refresh_habit_list()

    def complete_habit(self):
        """Marks the selected habit as complete for the current day."""
        selection = self.habit_listbox.curselection()
        if selection:
            habit_name = self.habit_listbox.get(selection[0]).split(" (")[0]
            self.manager.mark_habit_complete(habit_name)
            self.refresh_habit_list()

    def show_analytics(self):
        """Displays a popup window with analytics about user habits."""
        streaks = get_longest_streak_all(self.manager)
        frequent = get_most_frequent_habit(self.manager)
        lines = [f"Longest Streaks:"]
        lines += [f"- {name}: {days} days" for name, days in streaks.items()]
        lines.append("")

        if frequent:
            lines.append(f"Most Frequent Habit: {frequent.name} ({len(frequent.checkoffs)} completions)")
            lines.append(f"Completion Rate: {get_completion_rate(frequent)}%")
            lines.append(f"Weekly Average: {get_weekly_average(frequent)} times/week")

        messagebox.showinfo("Habit Analytics", "\n".join(lines))

    def quit_app(self):
        """Saves all data and closes the GUI application."""
        self.manager.save_data()
        self.root.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    app = HabitApp(root)
    root.mainloop()
