def calculate_finances(income, rent, utilities, groceries, transportation, savings_rate):
   
    total_expenses = rent + utilities + groceries + transportation
    
    savings_amount = income * savings_rate / 100
    
    remaining_amount = income - total_expenses - savings_amount
    
    rent_percent = (rent / income) * 100
    utilities_percent = (utilities / income) * 100
    groceries_percent = (groceries / income) * 100
    transportation_percent = (transportation / income) * 100
    savings_percent = (savings_amount / income) * 100
    
    return {
        'savings_amount': savings_amount,
        'remaining_amount': remaining_amount,
        'rent_percent': rent_percent,
        'utilities_percent': utilities_percent,
        'groceries_percent': groceries_percent,
        'transportation_percent': transportation_percent,
        'savings_percent': savings_percent
    }

def main():
    print("Personal Finance Calculator")

    income = input("Enter your monthly income: ")
    rent = input("Enter your monthly rent/mortgage: ")
    utilities = input("Enter your monthly utilities expense: ")
    groceries = input("Enter your monthly groceries expense: ")
    transportation = input("Enter your monthly transportation expense: ")
    savings_rate = input("Enter the percentage of your income you want to save: ")

    results = calculate_finances(income, rent, utilities, groceries, transportation, savings_rate)

    print("\nFinancial Summary:")
    print(f"Total Savings Amount: ${results['savings_amount']:.2f}")
    print(f"Remaining Amount to Spend: ${results['remaining_amount']:.2f}")
    print(f"Rent/Mortgage: {results['rent_percent']:.2f}% of income")
    print(f"Utilities: {results['utilities_percent']:.2f}% of income")
    print(f"Groceries: {results['groceries_percent']:.2f}% of income")
    print(f"Transportation: {results['transportation_percent']:.2f}% of income")
    print(f"Savings: {results['savings_percent']:.2f}% of income")

if __name__ == "__main__":
    main()
    