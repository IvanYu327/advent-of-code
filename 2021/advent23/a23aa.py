from copy import deepcopy

def readFile():
    file = "advent23/info.txt"

    arr = []

    with open(file) as f:
        for readline in f:
            t = []
            for x in readline.strip():
                t.append(x)
            arr.append(t)
            
    return arr

solutions = []

def solve(b,solution):
    a = deepcopy(b)

    amphs = ["A","B","C","D"]
    rooms = [3,5,7,9]
    
    solved = True
    for x in range(2,4):
        for r in range(4):
            print(a[x][rooms[r]],amphs[r])
            if a[x][rooms[r]] != amphs[r]:
                solved = False
                break
    
    if solved:
        print("solved: "+str(solution))
        solutions.append(solution)

    for r in range(1,len(a)-1):
        for c in range(1,len(a[r])-1):
            x = a[r][c]
            if x in amphs:
                for rr in range(1,len(a)-1):
                    for cc in range(1,len(a[r])-1):
                        cell = a[rr][cc]
                        if cell == "." and 


    



if __name__ == "__main__":
    arr = readFile()

    for a in arr:
        print(a)
    
    s = solve(arr,[])