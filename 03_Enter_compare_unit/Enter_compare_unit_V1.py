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
    #check if unit has numbers in it
    if any(char.isdigit() for char in unit):
        #check if unit has "kg", "g", "ml" or "L" in it
        if "kg" or "g" or "ml" or "L" in unit:
            if "ml" or "g" in unit:
                # divide by 1000 to convert to Kg or L
                