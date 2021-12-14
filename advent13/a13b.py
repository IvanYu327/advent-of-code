from os import get_inheritable
import numpy as np

coords = []
instructions = []

with open('advent13/info.txt') as f:
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

size = max(max(x) for x in coords)+1

grid = [ [ "." for i in range(size) ] for j in range(size) ]

for coord in coords:
    grid[coord[1]][coord[0]] = "#"

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

xs = []
ys = []
for instruction in instructions:
    if instruction[0] == "y":
        ys.append(int(instruction[2:]))
    else:
        xs.append(int(instruction[2:]))

y = min(ys) + 1
x = min(xs) + 1

print(y,x)


for r in range(len(grid[r])):
    for t in range(x,size):
        grid[r].pop(x)

for r in range(y,size):
    grid.pop(y)

display(grid)