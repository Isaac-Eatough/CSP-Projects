def scan(type):
    return float(input(f"what is your {type}: "))
income = scan("income")
rent= scan("rent")
utilities = scan("utilities")
groceries = scan("groceries")
transportation = scan("transportation")
print("Hello and welcome to your finacial calculator!\n")
savings = income*.2
expenses = rent+utilities+groceries+transportation
spending = income-savings-expenses
def percent(type, amount):
    per = amount/income *100
    print(f"your {type} is {per}% income.")
print(f"your monthly income is ${income:.2f}\n")
print(f"your monthly expenses is ${expenses:.2f}\n")
print(f"your monthly savings is ${savings:.2f}\n")
print(f"your monthly spending money is ${spending:.2f}\n")
print(percent("rent",rent))
print(percent("utilities",utilities))
print(percent("groceries",groceries))
print(percent("transportation",transportation))
print(percent("savings",savings))
print(percent("expenses",expenses))