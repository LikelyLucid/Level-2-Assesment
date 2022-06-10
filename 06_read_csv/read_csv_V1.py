import csv

def search_csv(Item):
    #search for item in Items.csv
    with open('Items.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Item'] == Item:
                return row
    return None

print(search_csv('Banana'))