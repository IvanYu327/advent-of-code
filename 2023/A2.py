import numpy as np
import re

arr = []

with open('2023/input.txt', "r") as f:
    for readline in f: 
        line = readline.strip().split(": ")[1]

        line = line.split('; ')

        temp = []
        for x in line:
            temp.append(x.split(', '))
        
        arr.append(temp)


# PART 1

master = {"red": 12, "green":13, "blue": 14}

total = 0

for game_index in range(len(arr)):
    valid = True
    for hand in arr[game_index]:
        for cube in hand:
            count = cube.split(' ')
            if count[1] in master and int(count[0]) > master[count[1]]:
                valid = False
                break
        
    if valid:
        total += game_index + 1

print(total)

# PART 2

total = 0

for game in arr:
    game_cubes = {"red": 0, "green": 0, "blue": 0}

    for hand in game:
        for cube in hand:
            count = cube.split(' ')
            if int(count[0]) > game_cubes[count[1]]:
                game_cubes[count[1]] = int(count[0])
    
    power = 1
    for x in game_cubes.values():
        power *= x

    total += power
    
print(total)
