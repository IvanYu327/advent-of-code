from os import read


arr = []

with open('advent10/info.txt') as f:
    for readline in f:
        arr.append(readline.strip())

openers = ["(","[","{","<"]
closers = [")","]","}",">"]

print(arr)

illegal = ""

for line in arr:
    reader = ""
    for char in line:
        if char in openers:
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
                illegal+=char
                break

print(illegal)

score = illegal.count(")")*3 + illegal.count("]")*57 + illegal.count("}")*1197 + illegal.count(">")*25137
print (score)
