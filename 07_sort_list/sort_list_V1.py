list = [("banana", "g", "1", "1.50"),("coffee", "g", "1", "3")]

def calc_price(list):
    sorted_list = []
    #append to each tuple the price using the price divided by the weight
    for item in list:
        price = float(item[3])
        weight = float(item[2])
        total_price = (price/weight)
        item = item + (total_price,)


print(calc_price(list))