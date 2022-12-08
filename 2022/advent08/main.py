import numpy as np
import re

arr = []

with open('2022/advent08/input.txt', "r") as f:
    for readline in f: 
        line = readline.strip()
        temp = []
        for char in line:
            temp.append(int(char))

        arr.append(temp)

rows = len(arr)
cols = len(arr[0])

# PART 1
visible = [ [0]*cols for i in range(rows)]

for row in range(rows):
    
    lastVisible = -1
    for tree in range(cols):
        if arr[row][tree] > lastVisible:
            lastVisible = arr[row][tree]
            visible[row][tree] = 1
    
    lastVisible = -1
    for tree in range(cols):
        if arr[row][-tree-1] > lastVisible:
            lastVisible = arr[row][-tree-1]
            visible[row][-tree-1] = 1

for tree in range(cols):
    
    lastVisible = -1
    for row in range(rows):
        if arr[row][tree] > lastVisible:
            lastVisible = arr[row][tree]
            visible[row][tree] = 1
    
    lastVisible = -1
    for row in range(rows):
        if arr[-row-1][tree] > lastVisible:
            lastVisible = arr[-row-1][tree]
            visible[-row-1][tree] = 1

count = np.count_nonzero(np.array(visible) == 1)
print(count)


# PART 2
scores = [ [0]*cols for i in range(rows)]

for row in range(rows):
    for col in range(cols):
        max = arr[row][col]

        # UP
        upCount = 0
        for x in range(1,row+1):
            upCount += 1
            if arr[row-x][col] >= max:
                break
            
        # LEFT
        leftCount = 0
        for x in range(1,col+1):
            leftCount += 1
            if arr[row][col-x] >= max:
                break

        # RIGHT
        rightCount = 0
        for x in range(1,cols-col):
            rightCount += 1
            if arr[row][col+x] >= max:
                break

        # DOWN
        downCount = 0
        for x in range(1,rows-row):
            downCount += 1
            if arr[row+x][col] == max:
                break
            
        scores[row][col] = upCount*downCount*leftCount*rightCount

print(np.max(np.array(scores)))