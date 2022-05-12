# ask user for budget and if its an interger then convert it to float.
def check_float(question):
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter a valid number")

budget = input("Enter your budget: $")
while check_float(budget) == False:
    print("Please enter a valid number")
    budget = input("Enter your budget: $")
budget = float(budget)
print(budget)
