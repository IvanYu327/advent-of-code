import a15a as test

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

cave = readFile()
low = test.minPathSum(cave)

def minPathSum(r,c,length):
    m = len(cave);
    n = len(cave[0]);

    if r == m and c == n:
        return cave[r][c]   
    
    if r+1<m and length < low:
        return cave[r][c] + minPathSum(cave,r+1,c,length,low)
    
    if r-1>0 and length < low:
        return cave[r][c] + minPathSum(cave,r+1,c,length,low)
    
    if r+1<m and length < low:
        return cave[r][c] + minPathSum(cave,r+1,c,length,low)


if __name__ == "__main__":
    minPathSum(0,0)