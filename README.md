# Habit Tracker App

Track and analyze your daily or weekly habits via a command-line or graphical interface.

## Features
- Create, edit, delete and  view habits
- Mark habits as complete
- Analyze longest streaks, most frequent habits, completion rates
- Save/load habits with JSON storage
- Unit-tested with `pytest`
- GUI support using Tkinter (optional)

## Requirements
- Python 3.7+
- `pytest` (for testing)

## How to Use

### ▶ Run CLI App
```bash
cd habit_tracker
python main.py
```
**Menu Options:**
1. Create Habit  
2. List Habits  
3. Complete Habit  
4. Edit Habit  
5. Delete Habit  
6. Analytics  
7. Save & Exit

### 🖥️ Run GUI App (Tkinter) #Optional
```bash
python gui.py
```
**GUI Features:**
- View & manage habits
- Complete habits
- Analytics popup (streaks, rates, frequency)

### 🧪 Run Tests
```bash
pytest tests/test.py
pytest tests/test-analytics.py
```
Runs unit tests for habit logic, completion, analytics.

## 🗂️ Project Structure
```
habit_tracker/
├── main.py                # CLI interface
├── gui.py                 # Tkinter GUI (optional)
├── models/
│   └── habit.py           # Habit class
├── services/
│   ├── manager.py         # HabitManager class
│   └── analytics.py       # Functional analytics
├── data/
│   └── habits.json   # User data (saving habits)
│   └── habits_data.json   # preloaded + new User created data (saved habits)
├── fixtures/
│   └── example_data.json   # preloaded user data (saved habits)
├── tests/
│   └── test.py        # Unit tests
    └── test_analytics.py        # Unit tests specifcally for analytics (optional)
└── README.md          #contains instructions for running and testing the app
```

## 📌 Notes
- First run loads habits data from `fixtures/example_data.json`.

---
Built with using OOP + Functional Programming in Python.
