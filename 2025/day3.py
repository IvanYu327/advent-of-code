from utils import get_input
from math import floor, ceil

data = get_input(3)

n = len(data[0])
joltage = 0

def largest_k_subsequence(nums, k):
    drop = len(nums) - k
    stack = []

    for d in nums:
        while drop > 0 and stack and stack[-1] < d:
            stack.pop()
            drop -= 1
        stack.append(d)

    return stack[:k]

for line in data:
    line = [int(i) for i in line]
    j = largest_k_subsequence(line, 12)
    j = int("".join(map(str, j)))
    joltage += j


print(joltage)