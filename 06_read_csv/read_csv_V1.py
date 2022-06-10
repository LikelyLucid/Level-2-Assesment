import csv

def search_csv(Item):
    #search for item in Items.csv
    with open('Items.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row[0] == Item:
                return row
    return None

print(search_csv('Banana'))
item = search_csv('Banana')
if item is None:
    print('Item not found')
else:
    print("item:" item[])