arr = []

with open('advent9/info.txt') as f:
    for readline in f:
        temp = []
        for i in readline.strip():
            temp.append(int(i))
        arr.append(temp)

print(arr)

total = 0

for r in range(len(arr)):
    for c in range(len(arr[r])):
        isLow = True
        if c+1<len(arr[r]) and arr[r][c+1]<=arr[r][c]:
            isLow = False
        elif c-1>=0 and arr[r][c-1]<=arr[r][c]:
            isLow = False
        elif r+1<len(arr) and arr[r+1][c]<=arr[r][c]:
            isLow = False
        elif r-1>=0 and arr[r-1][c]<=arr[r][c]:
            isLow = False
        
        if isLow:
            total += 1 + arr[r][c]

print(total)