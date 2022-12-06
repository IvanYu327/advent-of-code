import numpy as np
import re

arr = []

with open('2022/advent04/input.txt', "r") as f:
    for readline in f: 
        arr.append(re.split(r",|-", readline.strip()))


# PART 1
count = 0
for pair in arr:
    aStart = int(pair[0])
    aEnd = int(pair[1])
    bStart = int(pair[2])
    bEnd = int(pair[3])

    if aStart >= bStart and aStart <= bEnd and aEnd >= bStart and aEnd <= bEnd:
        count+=1
    elif bStart >= aStart and bStart <= aEnd and bEnd >= aStart and bEnd <= aEnd:
        count+=1


print(count)
# PART 2

count = 0
for pair in arr:
    aStart = int(pair[0])
    aEnd = int(pair[1])
    bStart = int(pair[2])
    bEnd = int(pair[3])

    if (aStart >= bStart and aStart <= bEnd) or (aEnd >= bStart and aEnd <= bEnd):
        count+=1
    elif (bStart >= aStart and bStart <= aEnd) or (bEnd >= aStart and bEnd <= aEnd):
        count+=1

print(count)