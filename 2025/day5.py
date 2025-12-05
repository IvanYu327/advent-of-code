from utils import get_input
from math import floor, ceil

data = get_input(5)


ranges = []
items = []
t = False
for line in data:
    if line == '':
        t = True
        continue
    
    if not t:
        ranges.append([int(x) for x in line.split("-")])
    else:
        items.append(int(line))

part1 = 0
for item in items:
    for r in ranges:
        if item in range(r[0], r[1]+1):
            part1 += 1
            break



print("Part 1: ", part1)

part2 = 0
ranges.sort()

merged_ranges = []

for r in ranges:
    if not merged_ranges:
        merged_ranges.append(r)
    else:
        if r[0] <= merged_ranges[-1][1]:
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], r[1]))
        else:
            merged_ranges.append(r)

part2 = 0
for r in merged_ranges:
    part2 += r[1] - r[0] + 1

print("Part 2: ", part2)