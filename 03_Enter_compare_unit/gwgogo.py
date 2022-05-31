import random
list = []

for i in range(5):
    value1 = random.randint(1, 10)
    value2 = random.randint(1, 10)
    value3 = random.randint(1, 10)
    list.append([value1, value2, value3])
print(list)

high = 0

for item in list: # repeat for each item in list
    itemval = item[1] # grab the first number in the list
    # print(itemval)
    # print(item)
    if itemval > high:
        high = itemval
        best = item


print(best)