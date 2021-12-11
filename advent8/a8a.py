arr = []

with open('advent8/info.txt') as f:
    for readline in f:
        temp = readline.split("|")
        arr += temp[1].split()

print(arr)
print(len(arr))

count = 0
for dig in arr:
    if int(len(dig)) in [2,4,3,7]:
        count+=1


print(count)