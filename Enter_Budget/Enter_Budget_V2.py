# ask user for budget and if its an interger then convert it to float.
def check_float(question):
    while True:
        try:
            float_num = input(question)
            return float(float_num)

        except ValueError:
             if float_num == "X" or "x":
                    break
            print("Please enter a valid number")

print(check_float("What is your budget? "))
