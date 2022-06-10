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
        writer = csv.writer(outfile)
        writer.writerow(data.values())

append_list('Banana', 'g', '1', '1.50')