with open('advent2/info.txt') as f:
    lines = f.readlines()

h = 0
v = 0

for x in lines:
    temp = x.split()
    if temp[0] == "forward":
        h = h + int(temp[1])
    if temp[0] == "up":
        v = v - int(temp[1])
    if temp[0] == "down":
        v = v + int(temp[1])

print(h*v)