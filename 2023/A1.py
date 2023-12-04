import numpy as np
import re

arr = []

with open('2023/input.txt', "r") as f:
    for readline in f: 
        line = re.sub(r'\D', '', readline.strip())
        arr.append(line)

# PART 1

total = 0

for line in arr:
    if len(line) == 0:
        continue
    if len(line) == 1:
        total += int(line + line)
        continue
    num = line[0] + line[-1]

    total += int(num)
print("Part 1: ", total)



# PART 2

arr = []

with open('2023/input.txt', "r") as f:
    for readline in f: 
        line = readline.strip()
        arr.append(line)

total = 0

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


for line in arr:
    
    for i in range(len(numbers)):
        line = line.replace(numbers[i], numbers[i][0] + str(i+1) + numbers[i][-1])
    
    line = re.sub(r'\D', '', line)

    num = 0
    num = int(line[0] + line[-1])

    total += int(num)

print("Part 2: ",total)
