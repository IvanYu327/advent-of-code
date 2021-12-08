arr = []

with open('advent1/info.txt', "r") as f:
    for readline in f: 
        arr.append(int(readline.strip()))

inc = 0

for x in range(len(arr)-1):
    if arr[x] < arr[x+1]:
        inc += 1

print(inc)