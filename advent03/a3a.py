arr = []

with open('advent3/info.txt') as f:
    for readline in f: 
        arr.append(readline.strip())


g = [0,0,0,0,0,0,0,0,0,0,0,0]
e = [0,0,0,0,0,0,0,0,0,0,0,0]
count = 0

for num in arr:
    count += 1
    for x in range(12):
        if num[x] == "1":
            g[x]+=1

bin = list("000000000000")
bine = list("000000000000")

for x in range(12):
    if g[x]>count/2:
        bin[x] = "1"
    else:
        bine[x] = "1"

temp = ""
bin = temp.join(bin)
bine = temp.join(bine)

print(bin)
print(bine)

print(int(bin,2)*int(bine,2))