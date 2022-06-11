def check_float(question):
    while True:
        try:
            float_num = input(question) # ask question
            return float(float_num) # convert to float and return it

        except ValueError: # if not a float then ask again
            print("Please enter a valid number")

def Check_Blank(question):
    while True:
        text = input(question)  # ask question
        if text != "" and text.isnumeric() == False:  # if text isn't empty then return it
            return text
        else:  # if text is empty then ask again
            print("Please enter a valid name.")