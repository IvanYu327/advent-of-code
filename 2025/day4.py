from utils import get_input
from math import floor, ceil

data = get_input(4)

grid = [[x for x in line] for line in data]

ROWS = len(grid)
COLS = len(grid[0])

for row in grid:
    print(row)

def is_valid(grid, r, c):
    # cell has fewer than 4 '@'s around it
    count = 0
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if i == r and j == c:
                continue
            if i >= 0 and i < ROWS and j >= 0 and j < COLS:
                if grid[i][j] == '@':
                    count += 1
    return count < 4

# Part 1
count = 0
for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == '@':
            if is_valid(grid, row, col):
                count += 1
print("Part 1: ", count)

# Part 2
count = 0
removed = True
while removed:
    removed = False
    to_remove = []
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] == '@':
                if is_valid(grid, row, col):
                    to_remove.append((row, col))
    
    for row, col in to_remove:
        grid[row][col] = '.'
    
    count += len(to_remove)
    
    if to_remove:
        removed = True

print("Part 2: ", count)