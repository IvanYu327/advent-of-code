import numpy as np

round1 = []

for x in range(1,4):
    for z in range(9):
        round1.append(x)

round2 = []

for z in range(3):
    for x in range(9):
        round2.append(int(x/3)+1)

round3 = []

for z in range(9):
    for x in range(1,4):
        round3.append(x)






round1 = np.array(round1)
round2 = np.array(round2)
round3 = np.array(round3)

print(round1)
print(round2)
print(round3)

combos = str(np.add(np.add(round1,round2),round3))

print(combos)

for x in range(3,10):
    print(str(x)+": "+str(combos.count(str(x))))
