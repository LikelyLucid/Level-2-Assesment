import rich as rf

def main():
    budget = enter_budget()
    unit = enter_unit()
    unit_valid = check_unit(unit)
    while unit_valid == False:
        unit = enter_unit()
        unit_valid = check_unit(unit)
    product_name = enter_product_name()
    product_details = []
    while product_name != "X":
        number_of_units = enter_number_of_units()
        price = enter_price()
        price_per_unit = calculate_price_per_unit(number_of_units, price)
        product_details.append([product_name, number_of_units, price, price_per_unit])
        product_name = enter_product_name()
    product_details.sort(key=lambda x: x[3])
    print("\n")
    print("The cheapest item is:")
    rf.print_list(product_details[0])
    print("\n")
    print("The most expensive item is:")
    rf.print_list(product_details[-1])
    print("\n")
    print("The average unit price is:")
    rf.print_list(calculate_average_unit_price(product_details))
    print("\n")
    print("The items within budget are:")
    rf.print_list(show_items_within_budget(product_details, budget))
    print("\n")
    print("The items outside of budget are:")
    rf.print_list(show_items_outside_budget(product_details, budget))

def enter_budget():
    budget = input("Enter the maximum amount you want to spend: ")
    return budget

def enter_unit():
    unit = input("Enter the unit you want to compare by e.g. ml, kg, l, mg etc.: ")
    return unit

def check_unit(unit):
    valid_units = ["ml", "kg", "l", "mg"]
    if unit in valid_units:
        return True
    else:
        return False

def enter_product_name():
    product_name = input("Enter the product name: ")
    return product_name

def enter_number_of_units():
    number_of_units = input("Enter the number of units: ")
    return number_of_units

def enter_price():
    price = input("Enter the price: ")
    return price

def calculate_price_per_unit(number_of_units, price):
    price_per_unit = float(price) / float(number_of_units)
    return price_per_unit

def calculate_average_unit_price(product_details):
    total_price = 0
    for product in product_details:
        total_price += product[3]
    average_unit_price = total_price / len(product_details)
    average_unit_price = round(average_unit_price, 2)
    average_unit_price = str(average_unit_price)
    average_unit_price = [["Average unit price", average_unit_price]]
    return average_unit_price

def show_items_within_budget(product_details, budget):
    items_within_budget = []
    for product in product_details:
        if float(product[3]) <= float(budget):
            items_within_budget.append(product)
    return items_within_budget

def show_items_outside_budget(product_details, budget):
    items_outside_budget = []
    for product in product_details:
        if float(product[3]) > float(budget):
            items_outside_budget.append(product)
    return items_outside_budget

main()