list = [("banana", "g", "1", "1.50"),("coffee", "g", "1", "3")]

def calc_price(list):
    total = 0
    for item in list:
        total += float(item[3])
    return total