from expense import Expense


def main():
    
    expense_file_path = "expenses.csv"

    # Get user input for expense.
    # expense = get_user_expense()

    # Write expense to file.
    # save_expense_to_file(expense, expense_file_path)
    
    # Read file and summarize expense.
    summarize_expenses(expense_file_path)


def get_user_expense():
    print("Get user expense.")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: "))

    expense_categories = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ]

    while True:
        print("Select a category: ")
        for i, category_name in enumerate(expense_categories):
            print(f"\t{i + 1}. {category_name}")

        value_range = f"[1 - {len(expense_categories)}]"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid category. Please enter a valid category number.")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as file:
        file.write(f"{expense.name},{expense.category},{expense.amount}\n")


def summarize_expenses(expense_file_path):
    print("Summarizing user expense.")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses by category:")
    for key, amount in amount_by_category.items():
        print(f"\t{key}: ${amount:.2f}")


if __name__ == "__main__":
    main()
