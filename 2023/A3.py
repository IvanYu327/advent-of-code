import numpy as np
from utils import get_input
import re

# PART 1
grid = get_input()


symbol_locations = []

for row in range(len(grid)):
    for col in range(len(grid[row])):
        char = grid[row][col]

        if char != "." and not char.isnumeric():
            symbol_locations.append((row, col))


total = 0 
my_nums = []

for row in range(len(grid)):
    line = grid[row]
    num = ""

    for i in range(len(line)):
        if line[i].isnumeric():
            num += line[i]
        
        if num and (i + 1 == len(line) or not line[i + 1].isnumeric()):
            area_top_left = (row - 1, i - len(num))
            area_bottom_right = (row + 1, i + 1)
            
            for symbol in symbol_locations:
                if symbol[0] >= area_top_left[0] and symbol[0] <= area_bottom_right[0] and symbol[1] >= area_top_left[1] and symbol[1] <= area_bottom_right[1]:
                    total+= int(num)
                    my_nums.append(int(num))
                    break
                

            num = ""


print(total)



# PART 1
grid = get_input()


gear_locations = []

for row in range(len(grid)):
    for col in range(len(grid[row])):
        char = grid[row][col]

        if char == "*":
            gear_locations.append((row, col))


total = 0 
my_nums = []

for row in range(len(grid)):
    line = grid[row]
    num = ""

    for i in range(len(line)):
        if line[i].isnumeric():
            num += line[i]
        
        if num and (i + 1 == len(line) or not line[i + 1].isnumeric()):
            area_top_left = (row - 1, i - len(num))
            area_bottom_right = (row + 1, i + 1)
            
            for gear in gear_locations:
                if gear[0] >= area_top_left[0] and gear[0] <= area_bottom_right[0] and gear[1] >= area_top_left[1] and gear[1] <= area_bottom_right[1]:
                    total+= int(num)
                    my_nums.append(int(num))
                    break
                

            num = ""


print(total)

