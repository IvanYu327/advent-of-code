with open('advent2/info.txt') as f:
    lines = f.readlines()

h = 0
v = 0
aim = 0

for x in lines:
    temp = x.split()
    if temp[0] == "forward":
        h = h + int(temp[1])
        v = v + aim*int(temp[1])
    if temp[0] == "up":
        aim = aim - int(temp[1])
    if temp[0] == "down":
        aim = aim + int(temp[1])

print(h*v)