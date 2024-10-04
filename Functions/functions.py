
print("Hello and welcome to your finacial calculator!\n")
income =float(input("what is your monthly income: "))
rent =float(input("what is your monthly rent: "))
utilties =float(input("what is your monthly utilities: "))
groceries =float(input("what is your monthly groceries: "))
transportation =float(input("what is your monthly transportation cost: "))
savings = income*.2
expenses = rent+utilties+groceries+transportation
spending = income-savings-expenses
prent = income/rent *100
putilties = income/utilties *100
pgroceries = income/groceries *100
ptransportation = income/transportation *100
psavings = income/savings *100
pexpenses = income/expenses *100
def percent(type, amount):
    per = amount/income
    print(f"your {type} is {per}% income.")
print(f"your monthly income is ${income:.2f}\n")
print(f"your monthly expenses is ${expenses:.2f}\n")
print(f"your monthly savings is ${savings:.2f}\n")
print(f"your monthly spending money is ${spending:.2f}\n")
percent("rent",rent)
percent("utilities",utilties)
percent("rent",rent)
percent("rent",rent)
percent("rent",rent)
percent("rent",rent)