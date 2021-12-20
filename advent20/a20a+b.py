from os import P_WAIT
import numpy as np
from copy import deepcopy

# alg = "..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#"
alg = "#####.#.###.###.#.#.####.#####.####.#..####.##.####...##......#.##.##.#.#..#.##.###.#.#.#.##.#..#.####.#.#.##.#..........###.##...#.#...#.#.###..#...##.####.##...###.....##..##..##.#......#.#.##.#.#.##.#.......###.##.#.###.##..##.......##....#.##....#..###.######.##...##.##...#.#.##...##.##.#....##.####..#..#..##.##.#.#..#....#######.###.##...#.####..#.#.#.##...##..##.#.#.#.##.#.......###..######..###..##......###..###.#.#.#.......#.....##.#.##..#.##.#.##.####..#.##....##.#.#..#.####.##.#.#.##...#..##.####."

def readFile():
    file = "advent20/info.txt"

    array = []

    with open(file) as f:
        for readline in f:
            temp = []
            for x in readline.strip():
                if x == ".":
                    temp.append(0)
                else:
                    temp.append(1)
            # print(temp)
            array.append(temp)

    a = np.array(array)
    a = np.pad(a, pad_width=100)

    return a

def printA(array):
    print()
    for r in range(len(array)):
        for c in range(len(array[r])):
            dot = "."
            if array[r][c] == 1:
                dot = "#"
            print(" "+dot,end="")
        print()

def process(image):
    newImage = deepcopy(image)

    for r in range(1,len(image)-1):
        for c in range(1,len(image[r])-1):
            bit = ""
            for rr in range(r-1,r+2):
                for cc in range(c-1,c+2):
                    bit += str(image[rr][cc])
            
            bit = int(bit,2)
            
            light = 0
            if alg[bit] == "#":
                light = 1
            
            newImage[r][c]=light

    outer = 0
    if newImage[1][1] == 1:
        outer = 1

    for c in range(len(newImage[r])):
        newImage[0][c] = outer
        newImage[len(newImage)-1][c] = outer
    for r in range(len(newImage)):
        newImage[r][0] = outer
        newImage[r][len(newImage[r])-1] = outer

    # printA(newImage)
    print(np.count_nonzero(newImage))
    return newImage

if __name__ == "__main__":
    image = readFile()
    
    # printA(image)
    partA = 2
    partB = 50

    for x in range(partB):
        print(str(x+1)+"  ",end="")
        image = process(image)
