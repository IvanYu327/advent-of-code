from collections import Counter

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
    
    # print("now at:", end="")
    # print(currPath)

    if currPath[-1] == "end":# and currPath not in allPaths:
        allPaths.append(currPath)
    
    else:
    # elif currPath[-1] != "end":
        
        for link in links:

            if currPath[-1] == link[0]:

                allowed = True
                

                if link[1] == "start":
                    allowed = False
                elif not canEnterSmall(link[1],currPath[1:]):
                    allowed = False;
                
                if allowed:
                    # print(link[1])
                    findPaths(links,currPath+[link[1]])
 
def canEnterSmall(link,path):
    # print(link,path)
    if link not in path:
        # print(True)
        return True

    doesSmallTwiceExist = False
    for cave in path:
        if cave.islower() and dict(Counter(path))[cave] > 1:
            # print(dict(Counter(path))[cave])
            doesSmallTwiceExist = True

    if link.islower() and link in path and doesSmallTwiceExist:
        # print(False)
        return False
    else:
        # print(True)
        return True


if __name__ == "__main__":
    links = readFile()
    
    findPaths(links,["start"])

    print("done")
    # for path in allPaths:
    #     print(path)
        # print(dict(Counter(path)))
    
    print(len(allPaths))