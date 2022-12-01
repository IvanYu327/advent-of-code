order = [27,14,70,7,85,66,65,57,68,23,33,78,4,84,25,18,43,71,76,61,34,82,93,74,26,15,83,64,2,35,19,97,32,47,6,51,99,20,77,75,56,73,80,86,55,36,13,95,52,63,79,72,9,10,16,8,69,11,50,54,81,22,45,1,12,88,44,17,62,0,96,94,31,90,39,92,37,40,5,98,24,38,46,21,30,49,41,87,91,60,48,29,59,89,3,42,58,53,67,28]
# order = [49,48,98,84,71,59,37,36,6,21,46,30,5,33,3,62,63,45,43,35,65,77,57,75,19,44,4,76,88,92,12,27,7,51,14,72,96,9,0,17,83,64,38,95,54,20,1,74,69,80,81,56,10,68,42,15,99,53,93,94,47,13,29,34,60,41,82,90,25,85,78,91,32,70,58,28,61,24,55,87,39,11,79,50,22,8,89,26,16,2,73,23,18,66,52,31,86,97,67,40]


count = 0
moves = []
most = 0
mostBoard = []
mostChecked = []
def bingo(board):
    bingoBool = False
    # col check
    for col in range(5):
        colCheck = ""
        for (x) in range(5):
            colCheck += board[x][col]
        if len(colCheck) == 5:
            bingoBool = True


    # row check
    for row in range(5):
        rowCheck = ""
        for (x) in range(5):
            rowCheck += board[row][x]
        if len(rowCheck) == 5:
            bingoBool = True
    
    return bingoBool

while(True):
    
    
    board = []
    with open('advent4/info.txt') as f:
        for i, line in enumerate(f):
            if i >= count*6 and i < count*6+5:
                board.append(line.strip().split())        
    if board == []:
        break

    count += 1

    checked = [ [ "" for i in range(5) ] for j in range(5) ]

    for num in order:
        for row in range(0,5):
            for col in range(0,5):
                if int(board[row][col]) == num:
                    checked[row][col]="X"
        if bingo(checked) == True:
            print(count,order.index(num),most,board)
            if order.index(num)>most:
                most = order.index(num)
                mostBoard = board
                mostChecked = checked
            
            break
print(most)
print(mostBoard)
print(mostChecked)

unmarkedSum = 0
for row in range(0,5):
    for col in range(0,5):
        if mostChecked[row][col] == "":
            unmarkedSum+=int(mostBoard[row][col])

print(unmarkedSum,order[most])
print(unmarkedSum*order[most])






