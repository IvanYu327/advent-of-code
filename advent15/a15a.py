#failed but functioning attempt

#This one only works for if you are restricted to right and downwards movement


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

def minPathSum(cave):
    m = len(cave);
    n = len(cave[0]);
    pathChange = [[0 for x in range(m)] for y in range(n)]
    
    for r in range(1,m):
        pathChange[r][0] = pathChange[r-1][0]+cave[r][0]
    
    for c in range (1,n):
        pathChange[0][c] = pathChange[0][c-1]+cave[0][c]


    for r in range(1,m):
        for c in range(1,n):
            minPrev = min(pathChange[r-1][c],pathChange[r][c-1])
            pathChange[r][c] = minPrev+cave[r][c]
    
    printArr(pathChange)
    return pathChange[m-1][n-1]

if __name__ == "__main__":
    cave = readFile()
    printArr(cave)
    print(minPathSum(cave))