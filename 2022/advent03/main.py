import numpy as np

arr = []

with open('2022/advent03/input.txt', "r") as f:
    for readline in f: 
        arr.append(readline.strip())

# print(arr)

# PART 1

total = 0
key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for bag in arr:
    first = bag[:len(bag)//2]
    second = bag[len(bag)//2:]

    # print(bag)
    for item in first:
        if item in second:
            value = key.index(item)+1
            # print(item,value)
            total += value
            break


print(total)


# PART 2

total2 = 0

for x in range(0, len(arr), 3):
    first = arr[x]
    second = arr[x+1]
    third = arr[x+2]

    for item in first:
        if item in second and item in third:
            value = key.index(item)+1
            # print(item,value)
            total2 += value
            break

print(total2)