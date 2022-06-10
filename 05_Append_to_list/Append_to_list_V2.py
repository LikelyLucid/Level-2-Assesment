import csv

from black import NewLine
def append_list(Item, Unit, Weight, Price):
    #append items to Items.csv
    data = {
        "Item": Item,
        "Unit": Unit,
        "Weight": Weight,
        "Price": Price
    }
    with open('Items.csv', 'a', newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=data.keys())
        writer.writerow(data)

append_list('Banana', 'g', '1', '1.50')