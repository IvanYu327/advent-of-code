arr = []

with open('advent5/info.txt') as f:
    for readline in f: 
        temp = []
        temp = readline.strip().replace(" -> ",",").split(",")
        for t in temp:
            temp[temp.index(t)] = int(t)        
        arr.append(temp)


board = [ [ 0 for i in range(1000) ] for j in range(1000) ]


for line in arr:
    if line[0] == line[2]:
        for x in range(1000):
            if line[1] < line[3]:            
                if line[1] <= x <= line[3]:
                    board[line[0]][x]+=1
            if line[1] > line[3]:            
                if line[3] <= x <= line[1]:
                    board[line[0]][x]+=1


    if line[1] == line[3]:
        for x in range(1000):
            if line[0] < line[2]:            
                if line[0] <= x <= line[2]:
                    board[x][line[1]]+=1
            if line[0] > line[2]:            
                if line[2] <= x <= line[0]:
                    board[x][line[1]]+=1
    
    if line[1] != line[3] and line[0] != line[2]:
        print(line)
        if line[0] < line[2]:
            topRow = line[0]
            topCol = line[1]
            botRow = line[2]
            botCol = line[3]
        
        else:
            topRow = line[2]
            topCol = line[3]
            botRow = line[0]
            botCol = line[1]


        print(topRow,topCol,botRow,botCol)

        if topCol < botCol:            
            for step in range (botRow - topRow+1):
                board[topRow+step][topCol+step]+=1
                # print(topRow+step,topCol+step)
        if topCol > botCol:            
            for step in range (botRow - topRow+1):
                board[topRow+step][topCol-step]+=1

count = 0
for row in range(1000):
    for col in range(1000):
        if board[row][col] >=2:
            count+=1

print(count)