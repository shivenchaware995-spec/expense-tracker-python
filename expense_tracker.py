
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


# Add a new expense
def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


# View all expenses
def view_expenses():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        print("\n----- All Expenses -----")

        next(reader)  # Skip header

        for row in reader:
            print(
                f"Date: {row[0]} | "
                f"Category: {row[1]} | "
                f"Amount: ₹{row[2]} | "
                f"Description: {row[3]}"
            )


# Calculate total expenses
def total_expenses():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip header

        for row in reader:
            total += float(row[2])

    print(f"\nTotal Expenses: ₹{total:.2f}")


# Main program
def main():
    create_file()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            print("Thank you for using Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


main()