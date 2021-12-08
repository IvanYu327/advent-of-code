oArr = []
cArr = []

with open('advent3/info.txt') as f:
    for readline in f: 
        cArr.append(readline.strip())
        oArr.append(readline.strip())


for x in range(12):
    if len(oArr) == 1:
        break
    count1 = 0
    for num in oArr:
        if num[x] == "1":
            count1 +=1
    

    if count1*2 >= len(oArr):
        for z in range(1000):
            try:
                temp = oArr[999-z]
                if temp[x] == "0":
                    oArr.pop(999-z)
            except:
                a = 1
    else:
        for z in range(1000):
            try:
                temp = oArr[999-z]
                if temp[x] == "1":
                    oArr.pop(999-z)
            except:
                a = 1

print(oArr)
print(int(oArr[0],2))


for x in range(12):
    if len(cArr) == 1:
        break
    count1 = 0
    for num in cArr:
        if num[x] == "1":
            count1 +=1
    
    if count1 >= len(cArr)/2:
        for z in range(1000):
            try:
                temp = cArr[999-z]
                if temp[x] == "1":
                    cArr.pop(999-z)
            except:
                a = 1
    else:
        for z in range(1000):
            try:
                temp = cArr[999-z]
                if temp[x] == "0":
                    cArr.pop(999-z)
            except:
                a = 1

print(cArr)
print(int(cArr[0],2))

print(int(cArr[0],2)*int(oArr[0],2))