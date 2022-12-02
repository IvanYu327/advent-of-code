import numpy as np

arr = []

with open('2022/advent02/info.txt', "r") as f:
    for readline in f: 
        arr.append(readline.strip().split(" "))

# A rock Y paper
# B paper X rock
# C scisscor Z scissors

strat = {
    "X":1,#rock
    "Y":2,#paper
    "Z":3,#scissors
}

elfStrat = {
    "A":1,#rock
    "B":2,#paper
    "C":3,#scissors
}

score = 0

for match in arr:
    elf = match[0]
    me = match[1]

    if elf == "A" and me == "X":
        score += 3 + strat[me]
    elif elf == "A" and me == "Y":
        score += 6 + strat[me]
    elif elf == "A" and me == "Z":
        score += 0 + strat[me]

    elif elf == "B" and me == "X":
        score += 0 + strat[me]
    elif elf == "B" and me == "Y":
        score += 3 + strat[me]
    elif elf == "B" and me == "Z":
        score += 6 + strat[me]

    elif elf == "C" and me == "X":
        score += 6 + strat[me]
    elif elf == "C" and me == "Y":
        score += 0 + strat[me]
    elif elf == "C" and me == "Z":
        score += 3 + strat[me]


print(score)

# A rock X lose
# B paper Y draw
# C scisscor Z win

score = 0

for match in arr:
    elf = match[0]
    result = match[1]

    if result == "X":
    # lose
        myPlay = elfStrat[elf]-1
        if myPlay == 0:
            myPlay = 3

        score += myPlay + 0

    elif result == "Y":
    # draw
        score += elfStrat[elf] + 3
    elif result == "Z":
    # win
        score += elfStrat[elf]%3+1 + 6

print(score)