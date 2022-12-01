import numpy as np

arr = []

with open('advent10/info.txt') as f:
    for readline in f:
        arr.append(readline.strip())

incomplete = []

openers = ["(","[","{","<"]
closers = [")","}","}",">"]

for line in arr:
    reader = ""
    isIncomplete = True
    for char in line:
        if char in ["(","[","{","<"]:
            reader+=char
        else:
            if char == ")" and reader[-1] == "(":
                reader = reader[:-1]
            elif char == "]" and reader[-1] == "[":
                reader = reader[:-1]
            elif char == "}" and reader[-1] == "{":
                reader = reader[:-1]
            elif char == ">" and reader[-1] == "<":
                reader = reader[:-1]
            else:
                isIncomplete = False
                break
    
    if isIncomplete:
        incomplete.append(line)

pairs = ["()","[]","{}","<>"]

for line in incomplete:
    
    temp = line
    while(True): #remove all pairs, removing pairs will expose more pairs, remove them all until none left
        if any(x in temp for x in pairs):
            for pair in pairs:
                temp=temp.replace(pair,"")
        else:
            break
    
    lineScore = 0
    for char in reversed(temp):
        lineScore*=5
        lineScore+= openers.index(char)+1
    
    incomplete[incomplete.index(line)] = lineScore

incomplete = np.array(incomplete)
print(np.median(incomplete))