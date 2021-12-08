arr = []

with open('advent1/info.txt', "r") as f:
    for readline in f: 
        arr.append(int(readline.strip()))

newArr = []

for x in range(len(arr)-2):
    newArr.append(arr[x]+arr[x+1]+arr[x+2])

inc = 0

for x in range(len(newArr)-1):
    if newArr[x] < newArr[x+1]:
            inc = inc + 1

print(inc)