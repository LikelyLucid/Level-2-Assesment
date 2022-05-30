# ask user for Product name
def check_float(question):
    while True:
        try:
            float_num = input(question)
            return float(float_num)

        except ValueError:
            print("Please enter a valid number")


while True:
    print(check_float("What is your budget? "))