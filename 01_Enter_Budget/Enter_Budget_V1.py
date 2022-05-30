# ask user for budget and if its an interger then convert it to float.
def check_float(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


budget = input("Enter your budget: $")
while check_float(budget) == False:
    print("Please enter a valid number")
    budget = input("Enter your budget: $")
budget = float(budget)
print(budget)
