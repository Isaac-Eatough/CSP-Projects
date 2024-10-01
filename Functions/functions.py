def get_user_inputs():
    print("Hello, and welcome to your financial calculator!")

    # Input monthly income
    income = float(input("What is your monthly income: $"))

    # Input monthly expenses
    rent = float(input("What is your monthly rent: $"))
    utilities = float(input("What is your monthly utilities: $"))
    groceries = float(input("What is your monthly groceries: $"))
    transportation = float(input("What is your monthly transportation costs: $"))

    return income, rent, utilities, groceries, transportation

def calculate_finances(income, rent, utilities, groceries, transportation):
    # Calculate total expenses and savings
    expenses = rent + utilities + groceries + transportation
    savings = income * 0.20  # Assuming 20% savings rate
    spending = income - expenses - savings

    # Calculate percentages
    percentages = {
        "rent": (rent / income) * 100,
        "utilities": (utilities / income) * 100,
        "groceries": (groceries / income) * 100,
        "transportation": (transportation / income) * 100,
        "savings": (savings / income) * 100,
        "expenses": (expenses / income) * 100
    }

    return expenses, savings, spending, percentages

def main():
    # Get user inputs
    income, rent, utilities, groceries, transportation = get_user_inputs()

    # Calculate finances
    expenses, savings, spending, percentages = calculate_finances(income, rent, utilities, groceries, transportation)

    # Output results
    print(f"\nYour monthly income is ${income:.2f}")
    print(f"Your monthly expenses are ${expenses:.2f}")
    print(f"Your monthly savings is ${savings:.2f}")
    print(f"Your monthly spending money is ${spending:.2f}")
    print(f"Your rent is {percentages['rent']:.0f}% of your monthly income")
    print(f"Your utilities are {percentages['utilities']:.0f}% of your monthly income")
    print(f"Your groceries are {percentages['groceries']:.0f}% of your monthly income")
    print(f"Your transportation is {percentages['transportation']:.0f}% of your monthly income")
    print(f"Your savings are {percentages['savings']:.0f}% of your monthly income")
    print(f"Your expenses are {percentages['expenses']:.0f}% of your monthly income")

# Run the main function
if __name__ == "__main__":
    main()
