list = [("banana", "g", "3", "1.50"), ("coffee", "g", "1", "3"), ("orange", "g", "2", "5")]


def sort_list(list):
    new_list = []
    for item in list:
        price = float(item[3])  # convert the price to a float
        weight = float(item[2])  # convert the weight to a float
        total_price = price / weight  # calculate the price per weight
        item = item + (total_price,)  # add the price per weight to the tuple
        new_list.append(item)  # add the tuple to the list
    new_list.sort(key=lambda x: x[4])  # sort the list by the price per weight
    return new_list


print(sort_list(list))
