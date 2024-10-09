def percent(percent, type)
    print(f"what is your {type}: ")
print("Hello and welcome to your finacial calculator!\n")
income = input(percent("monthly income" income))
rent = input(percent("monthly rent" rent))
utilties = input(percent("monthly utilities" utilities))
groceries = input(percent("monthly groceries" groceries))
transportation = input(percent("monthly transportation" transportation))
savings = income*.2
expenses = rent+utilties+groceries+transportation
spending = income-savings-expenses
def percent(type, amount):
    per = amount/income
    print(f"your {type} is {per}% income.")
print(f"your monthly income is ${income:.2f}\n")
print(f"your monthly expenses is ${expenses:.2f}\n")
print(f"your monthly savings is ${savings:.2f}\n")
print(f"your monthly spending money is ${spending:.2f}\n")
print(percent("rent",rent))
print(percent("utilities",utilties))
print(percent("groceries",groceries))
print(percent("transportation",transportation))
print(percent("savings",savings))
print(percent("expenses",expenses))