import csv
import rich
from rich.console import Console
from rich import print
from rich.table import Table

choice = ""
item_list = []

console = Console()

def pg_break():
    print("\n")
    print("=" * 40)
    print("\n")

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
        if text.isalpha():  # if text isn't empty then return it
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
        for row in reader: # for each row in the csv file
            if row[0] == Item:
                item_rows.append(row) # append the row to the list
    if len(item_rows) == 0:
        return None
    else:
        return item_rows # return the list


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

def final_table(Title, list): # create a table with the list
    table = Table(title=Title) # create a table
    table.add_column("Name")
    table.add_column("Weight")
    table.add_column("Price")
    table.add_column("Price per Kg")
    for item in list:
        table.add_row(str(item[0]), str(item[2]), str(item[3]), str(round(item[4], 2))) # Name, Weight, Price, Price per Kg
    console.print(table) # print the table

budget = check_float("Enter the budget: $ ")
console.print("\nEnter 'x' to exit when entering product name\n", style="underline bold red")
while True:
    product_name = Check_Blank(
        "Enter the product name: "
    ).lower()  # get the product name

    if product_name == "x":
        break  # if the user enters x then break the loop

    if search_csv(product_name) is not None:  # if the product name is found in the csv
        csv_list = search_csv(product_name)  # get the list of the product name
        console.print(
            "\nProduct has been entered before\n", style="bold green"
        )  # print that the product has been entered before
        choice = ""  # reset the choice

        while choice != "y" and choice != "n":  # while the choice is not y or n
            choice = input(
                "Would you like to autocomplete? (y/n): "
            ).lower()  # get the choice

        if choice == "y":  # if the choice is y
            if len(csv_list) == 1:  # if the list has only one item
                item_list.append(csv_list[0])  # append the item to the item list
                pg_break()
                continue

            else:  # if the list has more than one item
                loop = 0  # loop counter
                table = Table(
                    title="Autocomplete options"
                )  # create a table with the autocomplete options
                table.add_column("Option", style="cyan")
                table.add_column("Name")
                table.add_column("weight")
                table.add_column("Price")  # add columns to the table

                for item in csv_list:  # for each item in the list
                    # print(loop, item)
                    name = item[0]  # get the name
                    weight = str(item[2]) + " " + item[1]  # get the weight
                    price = "$" + str(item[3])  # get the price
                    table.add_row(
                        str(loop), name, weight, price
                    )  # add rows to the table
                    loop += 1  # increment the loop counter

                console.print(table)  # print the table
                choice = int(input("\nEnter the number of the item: "))
                item_list.append(csv_list[int(choice)])
                pg_break()
                continue

    unit, amount = get_unit()
    price = check_price()
    append_list(product_name, unit, amount, price)
    item_list.append([product_name, unit, amount, price])
    pg_break()


item_list = sort_list(item_list)
within, outside = sort_list_budget(item_list, budget)
pg_break()
# print each list as a table
if len(within) > 0:
    final_table("Within budget", within)
print()
if len(outside) > 0:
    final_table("Outside Budget", outside)
