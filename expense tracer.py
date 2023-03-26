import csv

# Define a function to add an expense to the CSV file
def add_expense(category, amount):
    with open("expenses.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([category, amount])

# Define a function to calculate the total expenses in a given category
def calculate_total(category):
    total = 0
    with open("expenses.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == category:
                total += float(row[1])
    return total

# Main loop for the expense tracker
print("Welcome to the expense tracker!")
while True:
    print("What would you like to do?")
    print("1. Add expense")
    print("2. Calculate total expenses")
    print("3. Exit")
    choice = input("> ")
    if choice == "1":
        category = input("Enter the category of the expense: ")
        amount = input("Enter the amount of the expense: ")
        add_expense(category, amount)
        print("Expense added successfully!")
    elif choice == "2":
        category = input("Enter the category of expenses to calculate: ")
        total = calculate_total(category)
        print(f"Total expenses in {category}: {total:.2f}")
    elif choice == "3":
        break
    else:
        print("Invalid choice, please try again.")
