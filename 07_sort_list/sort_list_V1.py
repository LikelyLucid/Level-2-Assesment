list = [("banana", "g", "1", "1.50"),("coffee", "g", "1", "3")]

def calc_price(list):
    #append to each tuple the price using the price divided by the weight
    for item in list:
        item_price = float(item[3])/float(item[2])
        item = item + (item_price,)
    return list
print