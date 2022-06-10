import csv

def search_csv(Item):
    #search for item in Items.csv
    with open('Items.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row['A'] == Item:
                return row
    return None

print(search_csv('Banana'))