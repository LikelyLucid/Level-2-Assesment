import csv
def append_list(Item, Unit, Weight, Price):
    #append items to Items.csv
    data = {
        "Item": Item,
        "Unit": Unit,
        "Weight": Weight,
        "Price": Price
    }
    with open('Items.csv', 'a') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=data.keys(), newline)
        writer.writerow(data)

append_list('Banana', 'g', '1', '1.50')