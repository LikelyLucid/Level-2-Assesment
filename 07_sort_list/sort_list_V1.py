list = [("banana", "g", "1", "1.50"),("coffee", "g", "1", "3")]

def calc_price(list):
    #append to each tuple the price using the price divided by the weight
    for item in list:
        print(item[3], item[2])
        item = list.append(float(str(item[3])) / float(str(item[2])))
calc_price(list)