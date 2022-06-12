import csv
import rich
from rich.console import Console
from rich import print
from rich.table import Table

choice = ""
item_list = []

console = Console()


def check_float(question):
    while True:
        try:
            float_num = console.input(question)  # ask question
            return float(float_num)  # convert to float and return it
        except ValueError:  # if not a float then ask again
            console.print("Please enter a valid number", style="underline bold red")


def Check_Blank(question):
    while True:
        text = input(question)  # ask question
        if (
            text != "" and text.isnumeric() == False
        ):  # if text isn't empty then return it
            return text
        else:  # if text is empty then ask again
            console.print("Please enter a valid name.", style="underline bold red")


def get_unit():
    while True:
        unit = input("Enter the unit\nKg, L, ml, g: ").lower()
        if unit not in ["kg", "l", "ml", "g"]:
            console.print("\nInvalid unit\n", style="underline bold red")
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
            console.print("\nInvalid price\n", style="underline bold red")


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
    item_rows = []
    # search for item in Items.csv
    with open("Items.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == Item:
                item_rows.append(row)
    if len(item_rows) == 0:
        return None
    else:
        return item_rows


def sort_list(list):
    new_list = []
    for item in list:
        price = float(item[3])  # convert the price to a float
        weight = float(item[2])  # convert the weight to a float
        total_price = price / weight  # calculate the price per weight
        item = tuple(item) + (total_price,)  # add the price per weight to the tuple
        new_list.append(item)  # add the tuple to the list
    new_list.sort(key=lambda x: x[4])  # sort the list by the price per weight
    return new_list


def sort_list_budget(list, budget):
    budget = float(budget)  # convert to float
    within_budget = []
    outside_budget = []
    for item in list:
        if float(item[3]) > budget:  # if the cost is greater than the budget
            outside_budget.append(item)  # append to the outside budget list
        else:
            within_budget.append(item)  # append to the within budget list
    return within_budget, outside_budget  # return the two lists


budget = check_float("Enter the budget: $ ")

while True:
    product_name = Check_Blank("Enter the product name: ").lower()
    if product_name == "x":
        break
    if search_csv(product_name) is not None:
        csv_list = search_csv(product_name)
        print("\nProduct has been entered before\n")
        choice = ""
        while choice != "y" and choice != "n":
            choice = input("Would you like to autocomplete? (y/n): ").lower()
        if choice == "y":
            if len(csv_list) == 1:
                item_list.append(csv_list[0])
            else:
                loop = 0
                for item in csv_list:
                    print(loop, item)
                    loop += 1
                choice = int(input("\nEnter the number of the item: "))
                item_list.append(csv_list[int(choice)])
    else:  # if the product is not in the csv
        unit, amount = get_unit()
        price = check_price()
        append_list(product_name, unit, amount, price)
        item_list.append([product_name, unit, amount, price])

item_list = sort_list(item_list)
within, outside = sort_list_budget(item_list, budget)
print("Items in your budget: ")
print(within)
print("Items outside your budget: ")
print(outside)
