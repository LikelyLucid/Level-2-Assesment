# ask user for budget and if its an interger then convert it to float.
def check_float(question):
    while True:
        try:
            float_num = input(question) # ask question
            return float(float_num) # convert to float and return it

        except ValueError:
            print("Please enter a valid number")


while True:
    print(check_float("What is your budget? "))
