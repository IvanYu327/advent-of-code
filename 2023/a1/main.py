import numpy as np
import re

arr = []

with open('2023/a1/input.txt', "r") as f:
    for readline in f: 
        line = re.sub(r'\D', '', readline.strip())
        # line = list(map(int, line))
        arr.append(line)

# PART 1

total = 0

for line in arr:
    if len(line) == 0:
        continue
    if len(line) == 1:
        total += int(line + line)
        continue
    num = line[0] + line[-1]

    print(line, num)
    total += int(num)
print(total)



# PART 2
