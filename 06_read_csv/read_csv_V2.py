import csv


def search_csv(Item):
    item_rows = []
    # search for item in Items.csv
    with open("Items.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        item_rows.extend(row for row in reader if row[0] == Item)
    if len(item_rows) == 0:
        return None
    else:
        return item_rows

print(search_csv("banana"))
