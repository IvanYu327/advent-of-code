def readFile():
    links = []

    with open('advent12/info.txt') as f:
        for readline in f:
            links.append(readline.strip().split("-"))

    for link in links:
        print(link)
    return links

def printArr(arr):
    for a in arr:
        print(a)
