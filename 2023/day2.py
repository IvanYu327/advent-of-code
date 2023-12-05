from utils import get_input
import numpy as np

input = get_input()

cards = []

for line in input:
    line = line.split(":")[1]
    line = line.split("|")

    win = line[0].strip().split(" ")
    nums = line[1].strip().split(" ")

    cards.append((win, nums))

# PART 1

total = 0
for card in cards:
    win = card[0]
    nums = card[1]

    points = 0

    for num in nums:
        if num and num in win:
            if points == 0:
                points = 1
            else:
                points *= 2
    
    total += points


print(total)


# PART 2

copies = [0 for x in range(len(cards))]
card_counts = [1 for x in range(len(cards))]
total = 0

for i in range(len(cards)):
    card = cards[i]
    index = i + 1
    win = card[0]
    nums = card[1]

    points = 0
    
    for num in nums:
        if num and num in win:
            copies[i] += 1

for i in range(len(copies)):
    count = copies[i]

    for c in range(1,count+1):
        if i+c < len(copies):
            card_counts[i+c] += card_counts[i]

for c in card_counts:
    total += c

print(total)
