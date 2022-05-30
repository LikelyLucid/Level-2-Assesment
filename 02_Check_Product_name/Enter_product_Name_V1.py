# ask user for Product name and if its empty then ask again.
def Check_Blank(question):
    while True:
        text = input(question)
        if text == "":
            print("Please enter a valid name")


while True:
    print(check_float("What is your budget? "))