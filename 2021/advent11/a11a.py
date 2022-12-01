
import numpy as np

arr = []

with open('advent11/info.txt') as f:
    for readline in f:
        arr.append([int(x) for x in readline.strip()])

# arr = np.array(arr)

for line in arr:
    print(line)

flashes = 0

for step in range(1,101):
    anotherPass = True
    
    print(step)

    for r in range(len(arr)):
        for c in range(len(arr[r])):
            arr[r][c]+=1

    while anotherPass:
        anotherPass = False


        
        for r in range(len(arr)):
            for c in range(len(arr[r])):
                if arr[r][c] > 9:
                    anotherPass = True
                    arr[r][c] = 0
                    flashes += 1
                    
                    if r-1 >= 0                                     and arr[r-1][c]   != 0:
                        arr[r-1][c]+=1
                    if r-1 >= 0         and c+1 < len(arr[r])       and arr[r-1][c+1] != 0:
                        arr[r-1][c+1]+=1
                    if                      c+1 < len(arr[r])       and arr[r]  [c+1] != 0:
                        arr[r][c+1]+=1
                    if r+1 < len(arr)   and c+1 < len(arr[r])       and arr[r+1][c+1] != 0:
                        arr[r+1][c+1]+=1
                    if r+1 < len(arr)                               and arr[r+1][c]   != 0:
                        arr[r+1][c]+=1
                    if r+1 < len(arr)   and c-1 >= 0                and arr[r+1][c-1] != 0:
                        arr[r+1][c-1]+=1
                    if                      c-1 >= 0                and arr[r]  [c-1] != 0:
                        arr[r][c-1]+=1
                    if r-1 >= 0         and c-1 >= 0                and arr[r-1][c-1] != 0:
                        arr[r-1][c-1]+=1
        
    for line in arr:
        print(line)
        
                    

print(flashes)