# This only worked for small cases
# not enough memory to brute force it oh no!
# see a22aa for my working solution

import numpy as np

def readFile():
    file = "advent22/info.txt"

    array = []

    with open(file) as f:
        for readline in f:
            readline = readline.strip()

            nums = []
            num = ""
            
            if readline[0:2] == "on":
                nums.append(1)
            else:
                nums.append(0)
            
            for x in readline.strip():
                if x.isnumeric() or x=="-":
                    # print(x)
                    num += x
                elif not x.isnumeric() and num != "":
                    nums.append(int(num))
                    num = ""
            nums.append(int(num))

            array.append(nums)

    min = np.min(array)
    array = array - min

    return array

def reboot(pGrid, coords):
    for coord in coords:
        print(coord)
        switch = coord[0]
        xs = [coord[1],coord[2]]
        ys = [coord[3],coord[4]]
        zs = [coord[5],coord[6]]
        
        for x in range(xs[0] , xs[1] + 1):
            for y in range(ys[0] , ys[1] + 1):
                for z in range(zs[0] , zs[1] + 1):
                    pGrid[x][y][z] = switch

        print(np.count_nonzero(pGrid))
    


if __name__ == "__main__":
    coords = readFile()

    max = np.max(coords) + 1
    powerGrid = np.zeros((max,max,max))


    # for coord in coords:
    #     print(coord)
    # print(max)

    reboot(powerGrid,coords)