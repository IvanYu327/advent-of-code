from utils import get_input

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
