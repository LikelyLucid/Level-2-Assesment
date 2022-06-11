def check_float(question):
    while True:
        try:
            float_num = input(question) # ask question
            return float(float_num) # convert to float and return it

        except ValueError: # if not a float then ask again
            print("Please enter a valid number")