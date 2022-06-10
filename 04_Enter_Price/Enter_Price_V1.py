def check_price():
    while True:
        try:
            price = float(input("Enter the price: $"))
            break
        except ValueError:
            print("\nInvalid price\n")

price = check_price()
print(price)