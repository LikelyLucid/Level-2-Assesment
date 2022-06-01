"""
1. Ask user to enter a Unit
2. Check if unit has numbers in it, if so then continue to step 4
3. if not then go to step 1
4. Get letters from the unit, e.g "kg" from "1kg" or "L" from "1L"
5. If letters are empty then go to step 1
6. If unit is "mg" or "g" or "ml" then convert to Kg and L respectively

an expected input is 15mg and the expected output is 0.015kg
"""


def check_unit(unit):
    while True:
        if (char.isdigit() for char in unit):
            print("has numbers")
            if "kg" in unit.lower():
                print("has kg or l")
            else:
                print("No Unit")
        else:
            print("No Number")
        unit = input("Enter a unit: ")


print(check_unit("10l"))
