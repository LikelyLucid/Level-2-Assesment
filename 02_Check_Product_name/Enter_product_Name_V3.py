# ask user for Product name and if its empty then ask again but allow for spaces in the text and numbers



def Check_Blank(question):
    while True:
        text = input(question) # ask question
        if text != "" or text == alphan: # if text isn't empty then return it
            return text
        else: # if text is empty then ask again
            print("Please enter a valid name.")


while True:
    print(Check_Blank("What is your product name? "))