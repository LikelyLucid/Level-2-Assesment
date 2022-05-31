import random
list = []

for i in range(5):
    value1 = random.randint(1, 10)
    value2 = random.randint(1, 10)
    value3 = random.randint(1, 10)
    list.append([value1, value2, value3])
print(list)

high = 0

for item[1] in list:
    if sum(item) > high:
        high = sum(item)