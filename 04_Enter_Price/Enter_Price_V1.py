def check_price():
    while True:
        price = float(input("Enter the price: "))
        if price > 0:
            return price