def check_price():
    while True:
        price = float(input("Enter the price: "))
        #if the price contains numbers then it will return the price
        if price > 0:
            return price
        #if the price is not a number then it will ask the user to enter a number again
        