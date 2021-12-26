def readFile():
    links = []

    with open('advent12/info.txt') as f:
        for readline in f:
            links.append(readline.strip().split("-"))

    for link in links:
        if link[::-1] not in links:
            links.append(link[::-1])

    return links

def printArr(arr):
    for a in arr:
        print(a)

allPaths = []

def findPaths(links,currPath):
    
    print("now at:", end="")
    print(currPath)

    if currPath[-1] == "end":
        allPaths.append(currPath)
    
    else:
        foundStep = False
        
        for link in links:

            if currPath[-1] == link[0]:
                foundStep = True
                allowed = True
                
                if link[1].islower() and link[1] in currPath:
                    allowed = False;
                
                if allowed:
                    print(link[1])
                    findPaths(links,currPath+[link[1]])

        print(foundStep) 
        if foundStep == False:
            print("failed path")



if __name__ == "__main__":
    links = readFile()

    # for link in links:
    #     print(link)
    
    findPaths(links,["start"])

    print("done")
    for path in allPaths:
        print(path)
    
    print(len(allPaths))