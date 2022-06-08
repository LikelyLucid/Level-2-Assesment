def check_price():
    while True:
        try:
            price = float(input("Enter the price: "))
            break
        except ValueError:
            

check_price()