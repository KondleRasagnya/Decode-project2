print("===== Expense Tracker =====")

total = 0

while True:
    expense = input("Enter expense (or type 'quit' to finish): ")

    if expense.lower() == "quit":
        break

    try:
        expense = float(expense)
        total += expense
        print(f"Current Total: ₹{total:.2f}")
    except ValueError:
        print("Invalid input! Please enter a number.")

print("\n===== Summary =====")
print(f"Total Spent: ₹{total:.2f}")
print("Thank you for using Expense Tracker!")