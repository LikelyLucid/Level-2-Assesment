import csv
def append_list(Item, Unit, Weight, Price):
    #append items to Items.csv
    data = {
        "Item": Item,
        "Unit": Unit,
        "Weight": Weight,
        "Price": Price
    }
    csv.