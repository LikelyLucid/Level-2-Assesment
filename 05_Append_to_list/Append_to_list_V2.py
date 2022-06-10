import csv

def append_list(Item, Unit, Weight, Price):
    #append items to Items.csv
    data = {
        "Item": Item,
        "Unit": Unit,
        "Weight": Weight,
        "Price": Price
    } #data is a dictionary
    with open('Items.csv', 'a', newline="") as outfile: # opens file in append mode
        writer = csv.DictWriter(outfile, fieldnames=data.keys())
        writer.writerow(data) # writes data to file

# used for testing
append_list('Banana', 'g', '1', '1.50')
append_list('Apple', 'g', '1', '1.50')
append_list('Orange', 'g', '1', '1.50')