def check_float(question):
    while True:
        try:
            float_num = input(question)  # ask question
            return float(float_num)  # convert to float and return it

        except ValueError:  # if not a float then ask again
            print("Please enter a valid number")


def Check_Blank(question):
    while True:
        text = input(question)  # ask question
        if (
            text != "" and text.isnumeric() == False
        ):  # if text isn't empty then return it
            return text
        else:  # if text is empty then ask again
            print("Please enter a valid name.")


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
            print("\nInvalid amount\n")

    if unit in ["ml", "g"]:
        amount = int(amount) / 1000

    return unit, amount

def check_price():
    while True:
        try:
            price = float(input("Enter the price: $"))
            return price
        except ValueError:
            print("\nInvalid price\n")

def append_list(Item, Unit, Weight, Price):
    # append items to Items.csv
    data = {
        "Item": Item,
        "Unit": Unit,
        "Weight": Weight,
        "Price": Price,
    }  # data is a dictionary
    with open("Items.csv", "a", newline="") as outfile:  # opens file in append mode
        writer = csv.DictWriter(outfile, fieldnames=data.keys())
        writer.writerow(data)  # writes data to file

