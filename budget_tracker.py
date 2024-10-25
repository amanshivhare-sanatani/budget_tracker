import csv
import os

# Define the filename for storing data
FILENAME = 'budget.csv'

# Load existing data from CSV
def load_data():
    budget_data = []
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                budget_data.append({'category': row[0], 'description': row[1], 'amount': float(row[2])})
    return budget_data

# Save data to CSV
def save_data(budget_data):
    with open(FILENAME, 'w', newline='') as file:
        writer = csv.writer(file)
        for entry in budget_data:
            writer.writerow([entry['category'], entry['description'], entry['amount']])

# Add a new expense
def add_expense(budget_data):
    category = input("Enter category (e.g., Food, Utilities, Entertainment): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    budget_data.append({'category': category, 'description': description, 'amount': amount})
    save_data(budget_data)
    print("Expense added successfully!")

# View total expenses per category
def view_expenses(budget_data):
    totals = {}
    for entry in budget_data:
        totals[entry['category']] = totals.get(entry['category'], 0) + entry['amount']
    
    print("\nTotal Spending by Category:")
    for category, total in totals.items():
        print(f"{category}: ${total:.2f}")

# Main program loop
def main():
    budget_data = load_data()
    print("Welcome to the Budget Tracker!")
    
    while True:
        print("\nOptions:")
        print("1. Add Expense")
        print("2. View Expenses by Category")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add_expense(budget_data)
        elif choice == '2':
            view_expenses(budget_data)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
