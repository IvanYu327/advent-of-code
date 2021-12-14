links = []

with open('advent12/info.txt') as f:
    for readline in f:
        links.append(readline.strip().split("-"))

for link in links:
    print(link)

paths = []

anotherPass = True
while anotherPass:
    temp = ["start"]
    anotherPass = False

    while True:
        for link in links:
            if temp[-1] == link[1]:
                temp.append(link[2])
                break
        
        if temp[-1] == "end":
            print(temp)
            if temp not in paths:
                anotherPass = True
                paths.append(temp)
                break


for p in paths:
    print(p)
