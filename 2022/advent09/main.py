import numpy as np
import re

arr = []

with open('2022/advent09/input.txt', "r") as f:
    for readline in f: 
        line = re.split(r" ", readline.strip())
        # line = list(map(int, line))
        line[1] = int(line[1])
        arr.append(line)


hPosition = [0,0]
tPosition = [0,0]
tVisited = []

# PART 1

for line in arr:
    direction = line[0]

    for x in range(line[1]):

        if direction == "U":
            hPosition[0] += 1
            if abs(hPosition[0] - tPosition[0]) > 1 or abs(hPosition[1] - tPosition[1]) > 1:
                tPosition = [hPosition[0]-1,hPosition[1]]
        elif direction == "D":
            hPosition[0] -= 1
            if abs(hPosition[0] - tPosition[0]) > 1 or abs(hPosition[1] - tPosition[1]) > 1:
                tPosition = [hPosition[0]+1,hPosition[1]]
        elif direction == "L":
            hPosition[1] -= 1
            if abs(hPosition[0] - tPosition[0]) > 1 or abs(hPosition[1] - tPosition[1]) > 1:
                tPosition = [hPosition[0],hPosition[1]+1]
        elif direction == "R":
            hPosition[1] += 1
            if abs(hPosition[0] - tPosition[0]) > 1 or abs(hPosition[1] - tPosition[1]) > 1:
                tPosition = [hPosition[0],hPosition[1]-1]


        if tPosition not in tVisited:
            tVisited.append(tPosition)

print(len(tVisited))



# PART 2

ropeLength = 10
ropePosition = [ [0]*2 for i in range(ropeLength)]
tVisited = []


for line in arr:
    # print(line)
    direction = line[0]

    for x in range(line[1]):
        # print(ropePosition)
        for segment in range(ropeLength):
            
            if segment == 0: #head
                if direction == "U":
                    ropePosition[segment][1] += 1
                elif direction == "D":
                    ropePosition[segment][1] -= 1
                elif direction == "L":
                    ropePosition[segment][0] -= 1
                elif direction == "R":
                    ropePosition[segment][0] += 1 
            
            elif abs(ropePosition[segment-1][0] - ropePosition[segment][0]) > 1 or abs(ropePosition[segment-1][1] - ropePosition[segment][1]) > 1:
                
                tempHead = ropePosition[segment-1]

                wantToGoTo = [  [tempHead[0]+1,tempHead[1]],
                                [tempHead[0]-1,tempHead[1]],
                                [tempHead[0],tempHead[1]+1],
                                [tempHead[0],tempHead[1]-1]  ]
                

                currX = ropePosition[segment][0]
                currY = ropePosition[segment][1]
                moved = False
                # print(segment,"|",currX,currY)
                
                for x in range(currX-1,currX+2):
                    for y in range(currY-1,currY+2):
                        if [x,y] in wantToGoTo:
                            # print(segment," moved to ",x,y)
                            ropePosition[segment]=[x,y]
                            moved = True
                            break
                    if moved:
                        break

                if not moved:
                    wantToGoTo = [  [tempHead[0]+1,tempHead[1]+1],
                                [tempHead[0]+1,tempHead[1]-1],
                                [tempHead[0]-1,tempHead[1]+1],
                                [tempHead[0]-1,tempHead[1]-1]  ]
                
                    for x in range(currX-1,currX+2):
                        for y in range(currY-1,currY+2):
                            if [x,y] in wantToGoTo:
                                # print(segment," moved to ",x,y)
                                ropePosition[segment]=[x,y]
                                moved = True
                                break
                        if moved:
                            break


            if ropePosition[9] not in tVisited:
                tVisited.append(ropePosition[9])

print(len(tVisited))
