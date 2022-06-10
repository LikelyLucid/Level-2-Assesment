list = [("banana", "g", "3", "1.50"),("coffee", "g", "1", "3")]

def calc_price(list):
    new_list = []
    #append to each tuple the price using the price divided by the weight
    for item in list:
        price = float(item[3])
        weight = float(item[2])
        total_price = (price/weight)
        item = item + (total_price,)
        new_list.append(item)
    return new_list

def sort_list(list):
    #sort the list by the price
    new_list = calc_price(list)
    new_list.sort(key=lambda x: x[4])
    return new_list

print(sort_list(list))