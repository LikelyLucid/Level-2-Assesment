
def get_unit():

    while True:
        unit = input("Enter the unit\nKg, L, ml, g: ").lower()
        if unit != "kg" and unit != "l" and unit != "ml" and unit != "g":
            print("Invalid unit")
        else:
            break

    while True:
        amount = input("Enter the amount: ")
        if amount.isnumeric():
            break
        else:
            print("Invalid amount")

    if unit == "ml" or unit == "g":
        