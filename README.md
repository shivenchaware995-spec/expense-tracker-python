# Expense Tracker

A simple beginner-friendly Expense Tracker built with Python.
It allows users to add expenses, view saved expenses, and calculate total spending.

## Features

* Add new expenses
* View all expenses
* Calculate total expenses
* Automatically save data in a CSV file
* Stores the date, category, amount, and description

## Technologies Used

* Python
* CSV
* datetime
* os

## Project Structure

```text
expense-tracker-python/
│
├── expense_tracker.py
├── README.md
└── expenses.csv
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/shivenchaware995-spec/expense-tracker-python.git
```

### 2. Open the project folder

```bash
cd expense-tracker-python
```

### 3. Run the program

```bash
python expense_tracker.py
```

## How It Works

The program provides a menu:

```text
===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Total Expenses
4. Exit
```

When adding an expense, the user enters:

* Category
* Amount
* Description

The expense is then saved in a CSV file.

## Example

```text
Enter your choice: 1
Enter category: Sport
Enter amount: 160
Enter description: Cricket bat and ball

Expense added successfully!
```

## Future Improvements

* Delete expenses
* Search expenses by category
* Monthly expense reports
* Expense charts and graphs
* Graphical user interface
* Export reports

## Author

**Shiven Chaware**

GitHub: https://github.com/shivenchaware995-spec
