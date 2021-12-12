from typing import Sized


arr = []

with open('advent9/info.txt') as f:
    for readline in f:
        temp = []
        for i in readline.strip():
            temp.append(int(i))
        arr.append(temp)

def check(r,c):
    basinSize = 1
    arr[r][c] = 9

    if c+1>len(arr[r])-1 or arr[r][c+1] == 9:
        if c-1<0 or arr[r][c-1] == 9:
            if r+1>len(arr)-1 or arr[r+1][c] == 9:
                if r-1<0 or arr[r-1][c] == 9:
                    return 1
    
    if c+1<len(arr[r]) and arr[r][c+1] != 9:
        basinSize+=check(r,c+1)
    if c-1>=0 and arr[r][c-1] != 9:
        basinSize+=check(r,c-1)
    if r+1<len(arr) and arr[r+1][c] != 9:
        basinSize+=check(r+1,c)
    if r-1>=0 and arr[r-1][c] != 9:
        basinSize+=check(r-1,c)
    
    return basinSize

biggest = [0,0,0]

for r in range(len(arr)):
    for c in range(len(arr[r])):
        if arr[r][c] != 9:
            basinSize = check(r,c)
            if basinSize > min(biggest):
                for x in range(len(biggest)):
                    if biggest[x] == min(biggest):
                        biggest[x] = basinSize
                        break

total = 1
for x in biggest:
    total*=x
print(total)
            




