from os import get_inheritable
import numpy as np

coords = []
instructions = []

with open('advent13/test.txt') as f:
    for readline in f:
        if readline.strip()!="" and readline.strip()[0] != "f":
            temp = readline.strip().split(",")
            coords.append([int(temp[0]),int(temp[1])])
        elif readline.strip()!= "":
            instructions.append(readline.strip().replace("fold along ",""))

def display(grid):
    for line in grid:
        for point in line:
            print(point+" ",end="")
        print()

size = np.amax(coords)+1

grid = [ [ "." for i in range(size) ] for j in range(size) ]

for coord in coords:
    print(coord)
    grid[coord[1]][coord[0]] = "#"


display(grid)
print(instructions)

for instruction in instructions:
    line = int(instruction[2:])

    if instruction[0] == "y":
        for r in range(line,len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "#":
                    grid [r][c] = "."
                    grid [line-(r-line)][c] = "#"
    else:
        for r in range(len(grid)):
            for c in range(line,len(grid[r])):
                if grid[r][c] == "#":
                    grid [r][c] = "."
                    grid [r][line-(c-line)] = "#"
    
    print(instruction)

    display(grid)

print(np.sum(np.char.count(grid, sub ='#')))