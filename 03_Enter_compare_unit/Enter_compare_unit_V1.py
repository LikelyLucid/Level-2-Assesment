def get_unit():

    while True:
        unit = input("Enter the unit\nKg, L, ml, g: ").lower()
        if unit not in ["kg", "l", "ml", "g"]:
            print("\nInvalid unit\n")
        else:
            break

    while True:
        amount = input("Enter the amount: ")
        if amount.isnumeric():
            break
        else:
            print("Invalid amount")

    if unit in ["ml", "g"]:
        amount = int(amount) / 1000

    return unit, amount


print(get_unit())
