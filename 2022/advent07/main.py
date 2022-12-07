import numpy as np
import re
import json

arr = []

with open('2022/advent07/input.txt', "r") as f:
    for readline in f: 
        line = re.split(r" |$ ", readline.strip())
        arr.append(line)

system = {"/":{}}

# PART 1
currPath = []
for cmd in arr:
    if cmd[0] == '$':
        if cmd[1] == "cd":
            if cmd[2] == "..":
                currPath.pop()
            elif cmd[2] == "/":
                currPath = ["/"]
            else:
                currPath.append(cmd[2])
    else:
        size = cmd[0]
        name = cmd[1]
        
        current = system
        
        for dir in currPath:
            if dir not in current:
                current[dir] = {}
            current = current[dir]
        
        if size == "dir":
            size = {}
        current.update({name: size})

# pretty = json.dumps(system, indent=2)
# print(pretty)

sizes = []

def returnSize (dir):
    total = 0

    for key in dir:
        if type(dir[key]) == dict:
            total += returnSize (dir[key])
        else:
            total += int(dir[key])
    
    sizes.append(total)
    return total

returnSize(system)

score = 0

for size in sizes:
    if size <= 100000:
        score += size

print(score)

# PART 2

totalSize =  70000000
mustBeFree = 30000000

totalSize = sizes[-1]
unusedSpace = totalSize - totalSize
spaceNeeded = mustBeFree - unusedSpace

toDelete = totalSize
for size in sizes:
    if size > spaceNeeded and size - spaceNeeded < toDelete - spaceNeeded:
        toDelete = size

print(toDelete)