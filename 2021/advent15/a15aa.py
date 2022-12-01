def readFile():
    file = "advent15/test.txt"
    # file = "advent15/info.txt"

    array = []
    with open(file) as f:
        for readline in f:
            temp = []
            for value in readline.strip():    
                temp.append(int(value))
            array.append(temp)
    return array

def printArr(arr):
    print()
    for line in arr:
        print(line)

minPathSum = 100

def findMinPathSum(cave,r,c,visited,sum = 0):
    global minPathSum

    rows = len(cave)
    cols = len(cave[0])
    print(rows,cols,sum)
    sum+=cave[r][c]
    visited+=[r,c]

    if r == rows-1 and c == cols - 1:
        print(f"found a sum {sum}")
        if sum < minPathSum:
            minPathSum = sum
    
    else:
        if r + 1 < rows and [r+1,c] not in visited:
            findMinPathSum(cave,r+1,c,visited,sum)
        if c + 1 < cols and [r,c+1] not in visited:
            findMinPathSum(cave,r,c+1,visited,sum)
        if r - 1 >= 0 and [r-1,c] not in visited:
            findMinPathSum(cave,r-1,c,visited,sum)
        if c - 1 >= 0 and [r-1,c-1] not in visited:
            findMinPathSum(cave,r,c-1,visited,sum)


if __name__ == "__main__":
    cave = readFile()
    
    print(minPathSum)

    findMinPathSum(cave,0,0,[[0,0]])

    print(minPathSum)