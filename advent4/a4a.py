order = [27,14,70,7,85,66,65,57,68,23,33,78,4,84,25,18,43,71,76,61,34,82,93,74,26,15,83,64,2,35,19,97,32,47,6,51,99,20,77,75,56,73,80,86,55,36,13,95,52,63,79,72,9,10,16,8,69,11,50,54,81,22,45,1,12,88,44,17,62,0,96,94,31,90,39,92,37,40,5,98,24,38,46,21,30,49,41,87,91,60,48,29,59,89,3,42,58,53,67,28]

count = 0
moves = []
least = 200
leastBoard = []
leastChecked = []
def bingo(board):
    for col in range(5):
        colCheck = ""
        for (x) in range(5):
            colCheck += board[x][col]
        if len(colCheck) == 5:
            return True

    for row in range(5):
        rowCheck = ""
        for (x) in range(5):
            rowCheck += board[row][x]
        if len(rowCheck) == 5:
            return True
    return False

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
            if order.index(num)<least:
                least = order.index(num)
                leastBoard = board
                leastChecked = checked
            
            break
print(least)
print(leastBoard)
print(leastChecked)

unmarkedSum = 0
for row in range(0,5):
    for col in range(0,5):
        if leastChecked[row][col] == "":
            unmarkedSum+=int(leastBoard[row][col])

print(unmarkedSum*order[least])






