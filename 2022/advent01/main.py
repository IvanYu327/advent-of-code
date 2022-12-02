import numpy as np

arr = []

with open('2022/advent01/input.txt', "r") as f:
    for readline in f: 
        arr.append(readline.strip())

elfTotals =  []
currentElfSum = 0

for calorie in arr:
    
    if calorie != '':
        currentElfSum += int(calorie)
    else:
        elfTotals.append(currentElfSum)
        currentElfSum = 0

print(np.max(elfTotals))

elfTotals.sort()

print(np.sum(elfTotals[-3:]))