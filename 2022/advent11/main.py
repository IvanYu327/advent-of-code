import numpy as np
import ast

monkeys = []

class Monkey:
    items = []
    operation = ""
    test = 0
    trueThrow = 0
    falseThrow = 0
    inspects = 0
    
    def __init__(self, items, operation, test, trueThrow, falseThrow):
        self.items = items
        self.operation = operation
        self.test = test
        self.trueThrow = trueThrow
        self.falseThrow = falseThrow

# Test
# monkeys.append(Monkey([79, 98],"*19",23,2,3))
# monkeys.append(Monkey([54, 65, 75, 74],"+6",19,2,0))
# monkeys.append(Monkey([79, 60, 97],"**2",13,1,3))
# monkeys.append(Monkey([74],"+3",17,0,1))


monkeys.append(Monkey([54, 53],"*3",2,2,6))
monkeys.append(Monkey([95, 88, 75, 81, 91, 67, 65, 84],"*11",7,3,4))
monkeys.append(Monkey([76, 81, 50, 93, 96, 81, 83],"+6",3,5,1))
monkeys.append(Monkey([83, 85, 85, 63],"+4",11,7,4))
monkeys.append(Monkey([85, 52, 64],"+8",17,0,7))
monkeys.append(Monkey([57],"+2",5,1,3))
monkeys.append(Monkey([60, 95, 76, 66, 91],"**2",13,2,5))
monkeys.append(Monkey([65, 84, 76, 72, 79, 65],"+5",19,6,0))


modNum = 1

for monkey in monkeys:
    modNum *= monkey.test

print(modNum)

# PART 1
# PART 2

rounds = 10000  #20 for part 1

for round in range(1,rounds+1):
    
    for monkey in monkeys:
        for item in monkey.items:
            item = eval(str(item)+monkey.operation)%modNum #//3 for part 1

            monkey.inspects += 1
            if item%monkey.test == 0:
                monkeys[monkey.trueThrow].items.append(item)
            else:
                monkeys[monkey.falseThrow].items.append(item)
    
        monkey.items = []

    
    if round in [1,20,1000] or round%1000 == 0:
        print("AFTER ROUND " +str(round))
        temp = [ monkeys[i].inspects for i in range(len(monkeys))]
        print(temp)
        

totalInspects = []

for monkey in monkeys:
    totalInspects.append(monkey.inspects)

totalInspects.sort()
print(totalInspects[-1]*totalInspects[-2])

