def get_user_inputs():
    """Get user inputs for monthly income and expenses."""
    print("Hello, and welcome to your financial calculator!\n")
    return [float(input(f"What is your monthly {field}: ")) for field in ["income", "rent", "utilities", "groceries", "transportation"]]

def main():
    """Run the financial calculator."""
    income, rent, utilities, groceries, transportation = get_user_inputs()
    expenses = rent + utilities + groceries + transportation
    savings = income * 100
    spending = income - expenses - savings

    print(f"\nYour monthly income is ${income:.2f}")
    print(f"Your monthly expenses are ${expenses:.2f}")
    print(f"Your monthly savings is ${savings:.2f}")
    print(f"Your monthly spending money is ${spending:.2f}")

    for label, cost in zip(["rent", "utilities", "groceries", "transportation", "savings", "expenses"], 
  [rent, utilities, groceries, transportation, savings, expenses]):
        print(f"Your {label} is {int(cost / income * 100)}% of your monthly income")

if __name__ == "__main__":
    main()
