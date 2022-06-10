import json

def append_list(Item, Unit, Weight, Price):
    #append items to Items.json
    data = {
        "Item": Item,
        "Unit": Unit,
        "Weight": Weight,
        "Price": Price
    }
    with open('Items.json', 'a') as outfile:
        json.dump(data, outfile, indent=4)

append_list('Banana', 'g', '1', '1.50')
file = open('Items.json', 'r')
