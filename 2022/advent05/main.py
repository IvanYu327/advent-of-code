import numpy as np
import re

arr = []

with open('2022/advent05/input.txt', "r") as f:
    for readline in f: 
        line = re.split(r"move | from | to", readline.strip())
        line = list(map(int, line[1:4]))
        arr.append(line)

#     [G] [R]                 [P]    
#     [H] [W]     [T] [P]     [H]    
#     [F] [T] [P] [B] [D]     [N]    
# [L] [T] [M] [Q] [L] [C]     [Z]    
# [C] [C] [N] [V] [S] [H]     [V] [G]
# [G] [L] [F] [D] [M] [V] [T] [J] [H]
# [M] [D] [J] [F] [F] [N] [C] [S] [F]
# [Q] [R] [V] [J] [N] [R] [H] [G] [Z]
#  1   2   3   4   5   6   7   8   9 


stacks = ["QMGCL"
, "RDLCTFHG"
, "VJFNMTWR"
, "JFDVQP"
, "NFMSLBT"
, "RNVHCDP"
, "HCT"
, "GSJVZNHP"
, "ZFHG"]


# PART 1
# ex: move 5 from 3 to 9
for step in arr:
    moveCount = step[0]
    start = step[1]-1
    end = step[2]-1

    for x in range(moveCount):
        item = stacks[start][-1]
        stacks[start] = stacks[start][:-1]
        stacks[end] = stacks[end] + item

result = ''

for stack in stacks:
    result += stack[-1]

print(result)

# PART 2
stacks = ["QMGCL"
, "RDLCTFHG"
, "VJFNMTWR"
, "JFDVQP"
, "NFMSLBT"
, "RNVHCDP"
, "HCT"
, "GSJVZNHP"
, "ZFHG"]

for step in arr:
    moveCount = step[0]
    start = step[1]-1
    end = step[2]-1
    
    items = ''

    # lmao its not efficient but its a modified part 1 for the sake of finishing the challenge fast too 
    for x in range(moveCount):
        item = stacks[start][-1]
        stacks[start] = stacks[start][:-1]
        items = item + items
    
    stacks[end] = stacks[end] + items

result = ''

for stack in stacks:
    result += stack[-1]

print(result)