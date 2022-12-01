from copy import deepcopy
from os import X_OK, truncate

def readFile():
    file = "advent25/info.txt"

    arr = []

    with open(file) as f:
        for readline in f:
            t = []
            for x in readline.strip():
                t.append(x)
            arr.append(t)
            
    return arr

def printA(arr):
    for line in arr:
        for x in line:
            print(x,end="")
        print()

def stepEast(arr):
    madeMove = False

    for r, rval in enumerate(arr):
        line = "" .join(arr[r])
        # print(line+"   ->   ",end="")

        if line[0] == "." and line[-1] == ">":
            line = line.replace(">.",".>")
            line = line[:-1] + "."
            line = ">" + line[1:]
            madeMove = True
        elif ">." in line:
            line = line.replace(">.",".>")
            madeMove = True

        # print(line)
    
        arr[r] = line
    return arr,madeMove

def stepSouth (arr):
    madeMove = False

    arr2 = deepcopy(arr)

    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if r!= len(arr)-1 and arr[r][c] == "v" and arr[r+1][c] =="." and arr2[r][c] == "v" and arr2[r+1][c] ==".":
                
                arr[r] = arr[r][:c] + "." + arr[r][c+1:]
                arr[r+1] = arr[r+1][:c] + "v" + arr[r+1][c+1:]
                madeMove = True
            elif r == len(arr)-1 and arr[r][c] == "v" and arr[0][c] =="." and arr2[r][c] == "v" and arr2[0][c] ==".":
                # print(r,c)
                # print(arr[r])
                # print(arr[0])
                # print(arr[r][:c] + "." + arr[r][c+1:])
                # print()

                arr[r] = arr[r][:c] + "." + arr[r][c+1:]
                arr[0] = arr[0][:c] + "v" + arr[0][c+1:]
                madeMove = True

    # for r in range(len(arr)):
    #     print(f"{arr2[r]}   ->   {arr[r]}")

    return arr,madeMove
            
            


if __name__ == "__main__":
    arr = readFile()
    # print("Initial state:")
    # printA(arr)

    step = 0
    while True:
        step+=1
        print(f"After {step} steps:")
        
        r1 = stepEast(arr)
        arr = r1[0]
        a = r1[1]
        
        r2 = stepSouth(arr)
        arr = r2[0]
        b = r2[1]
        
        
        if not a and not b:
            break
