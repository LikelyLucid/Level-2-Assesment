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
if search_csv('Banana') is None:
    print('Item not found')
else:
    print("item:" row[])