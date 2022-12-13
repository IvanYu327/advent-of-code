import numpy as np
import re

arr = []

with open('2022/advent10/input.txt', "r") as f:
    for readline in f: 
        line = re.split(r" ", readline.strip())
        arr.append(line)

# PART 1
signals = [[1,1]]

for line in arr:
    currSignal = signals[-1][1]
    
    instruction = line[0]
    signals.append([currSignal,currSignal])

    if instruction == "addx":
        signals.append([currSignal,currSignal+int(line[1])])

sum = 0
indexInterest = [20,60,100,140,180,220]

for i in indexInterest:
    sum += signals[i][0] * i

print(sum)





# PART 2

CRT = [ [0]*40 for i in range(6)]

for row in range(6):
    for col in range(1,41):
        index = row*40 + col
        
        if abs(signals[index][1] - col) <= 1:
            CRT[row][col-1] = '#'
        else:
            CRT[row][col-1] = '.'

for line in CRT:
    for pixel in line:
        print(pixel,end = "")
    print()