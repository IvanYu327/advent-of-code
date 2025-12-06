from utils import get_input
from math import floor, ceil

data = get_input(6, strip=False)

R = len(data)

# Part 1
lines = []

for line in data:
    temp = line.strip().split(' ')
    temp = [x for x in temp if x != '']
    lines.append(temp)

total = 0


for i in range(len(lines[0])):
    op = lines[R-1][i]

    exp = op.join([lines[j][i] for j in range(R-1)])
    total += eval(exp)

print('Part 1: ', total)

# Part 2
total = 0
nums = []
op = ''

for i in range(len(data[0])-1, -1, -1):
    num = ''
    for j in range(R-1):
        try:
            char = data[j][i]
        except:
            char = ' '

        if char.isspace():
            continue
        num += char
    try:
        maybe_op = data[R-1][i]
    except:
        maybe_op = ' '
    
    if maybe_op != ' ':
        op = maybe_op
    
    if not num and nums:
        exp = op.join(nums)
        total += eval(exp)
        nums = []
        op = ''
    elif num:
        nums.append(num)

exp = op.join(nums)
total += eval(exp)

print('Part 2: ', total)