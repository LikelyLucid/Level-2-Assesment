import csv


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
        return item_rows

print(search_csv("banana"))
