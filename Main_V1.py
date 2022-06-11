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

def search_csv(Item):
    # search for item in Items.csv
    with open("Items.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == Item:
                return row
    return None

def sort_list(list):
    new_list = []
    for item in list:
        price = float(item[3])  # convert the price to a float
        weight = float(item[2])  # convert the weight to a float
        total_price = price / weight  # calculate the price per weight
        item = item + (total_price,)  # add the price per weight to the tuple
        new_list.append(item)  # add the tuple to the list
    new_list.sort(key=lambda x: x[4])  # sort the list by the price per weight
    return new_list