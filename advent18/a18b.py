# reads the files and puts each snail number as an index in the array
def readFile():
    file = "advent18/info.txt"

    array = []

    with open(file) as f:
        for readline in f:
            
            array.append(readline.strip())
    return array

def add(a,b):
    return f"[{a},{b}]"

def findExplodable(number):
    for x in range(len(number)):
        test = ""
        
        leftNetBrackets = number[:x].count("[") - number[:x].count("]")
        if number[x] == "[" and number[x+1].isnumeric() and leftNetBrackets >= 4:            
            i = x
            test = number[x]
            while True:
                i += 1
                test += number[i]

                if test.endswith("["):
                    test = ""
                    break
                
                if test.endswith("]"):
                    break
            
            if test == "":
                return None
            else:
                return test


def explode(number,explodable):
    #print("    exploded:",end="")
    temp = explodable.replace("[","").replace("]","")
    temp = temp.split(",")
    exA = int(temp[0])
    exB = int(temp[1])
    
    for x in range(len(number)):       
        leftNetBrackets = number[:x].count("[") - number[:x].count("]")
        if leftNetBrackets>=4 and number[x] == "[":
            searchIndex = x
            break
    
    ind = number[searchIndex:].index(explodable)+searchIndex

    number = number[:searchIndex]+number[searchIndex:].replace(str(explodable),"0",1)
    for x in range(ind+1,len(number)):

        if number[x].isnumeric():
            num = number[x]
            i = x
            while True:
                i += 1
                if number[i].isnumeric():
                    num = num+number[i]
                else:
                    break
            
            number = number[:x] + str(exB+int(num)) + number[i:]
            break
    
    for x in range(ind-1,-1,-1):
    
        if number[x].isnumeric():
            num = number[x]
            i = x
            while True:
                i -= 1
                if number[i].isnumeric():
                    num = number[i]+num
                else:
                    break
            
            number = number[:i+1] + str(exA+int(num)) + number[x+1:]
            break

    #print(number)

    return number

def findSplit(number):
    for x in range(len(number)-2):
        twoChar = number[x]+number[x+1]
        if twoChar.isnumeric():
            return twoChar
    return None

def split(number,toSplit):
    #print("    splitted:",end="")
    
    a = int(int(toSplit)/2)
    b = int(int(toSplit)/2+0.5)
    replacement = f"[{a},{b}]"
    
    number = number.replace(toSplit,replacement,1)

    #print(number)
    return number


def reduce(number):
    #print("    Reducing: "+number)
    
    while True:
        
        while True:
            explodable = findExplodable(number)
            if explodable == None:
                break
            number = explode(number,explodable)

        toSplit = findSplit(number)
        if toSplit != None:
            explodable = "filler"
            number = split(number,toSplit)

        if explodable == None and toSplit == None:
            break
    
    return number

def findPair(number):
    for x in range(len(number)):
        test = ""
        if number[x] == "[" and number[x+1].isnumeric():            
            i = x
            test = number[x]
            while True:
                i += 1
                test += number[i]

                if test.endswith("["):
                    test = ""
                    break
                
                if test.endswith("]"):
                    break
            
            if test != "":
                return test

def magnitude(number):
    while True:
        pair = findPair(number)

        temp = pair.replace("[","").replace("]","")
        temp = temp.split(",")
        A = int(temp[0])
        B = int(temp[1])

        num = 3*A + 2*B

        number = number.replace(pair,str(num))
        #print(number)
        if number.isnumeric():
            return number


if __name__ == "__main__":
    numbers = readFile()

    maxMag = 0

    for a in range(len(numbers)):
        for b in range(len(numbers)):
            if a != b:
                print(a,b)
                total = add(numbers[a],numbers[b])
                total = reduce(total)
                mag = int(magnitude(total))
                if mag > maxMag:
                    maxMag = mag
    
    print(maxMag)
