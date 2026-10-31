# Student Expense & Budget Tracker

A simple Python CLI app to track student expenses and budget using JSON storage.

## Features

- Add expense (category, amount, description)
- View all expenses
- View summary (total expenses, budget, remaining)
- Set monthly budget
- Category-wise expense summary
- Input validation for category, amount, and budget
- Error handling for data file and CSV export
- Basic automated tests
- Export expenses to CSV

## How to run

1. Clone the repo:

```bash
git clone (https://github.com/anitasjana/student-expense-tracker.git)
```

2. Go to project folder:

```bash
cd student-expense-tracker
```

3. Run the app:

```bash
python main.py
```

## Example output

```text
=== Student Expense Tracker ===

1. Add expense
2. View all expenses
3. View summary (total, budget, remaining)
4. Set budget
5. Exit
6. Export expenses to CSV
Enter your choice (1/2/3/4/5/6): 3

=== Summary ===
Total expenses: 120.0
Budget: 7000.0
Remaining: 6880.0

Category-wise expenses:
Food : 120.0
```

## Future improvements

- Monthly filtering
- Simple charts
- GUI or web interface