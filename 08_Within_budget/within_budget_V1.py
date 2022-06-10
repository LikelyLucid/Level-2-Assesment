budget = 8

list = [('banana', 'g', '3', '1.50', 0.5), ('Tuy', 'g', '2', '5', 2.5), ('coffee', 'g', '1', '3', 3.0), ('apple', 'g', '1', '9', 9)]

def get_inside_budget(list, budget):
    new_list = []
    for item in list:
        price = float(item[3])
        weight = float(item[2])
        total_price = (price/weight)
        item = item + (total_price,)
        new_list.append(item)
    new_list.sort(key=lambda x: x[4])
    return new_list

