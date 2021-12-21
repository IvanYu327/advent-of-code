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

# old find explodable function, which had a flaw where if there was an explodable pair, it could be hidden
# by a pair of the same value that existed earlier in the list but was not within 4 nested pairs

# def findExplodable(number):
#     # print("finding ex")
#     explodable = []
    
#     for a in range(50):
#         for b in range(50):
#             test = [a,b]
#             stringTest = str(test).replace(" ","")
#             if stringTest in number:
#                 # print(stringTest)
#                 start = number.index(stringTest)
#                 end = start+len(stringTest)-1
#                 leftNetBrackets = number[:start].count("[") - number[:start].count("]")
#                 rightNetBrackets = number[end+1:].count("]") - number[end+1:].count("[")
#                 if leftNetBrackets>=4 and rightNetBrackets>=4:
#                     # print("    "+stringTest)
#                     explodable.append(test)

#     if explodable == []:
#         return None
#     else:
#         firstEx = []
#         for ex in explodable:
#             firstEx.append(number.index(str(ex).replace(" ","")))
#         firstEx = min(firstEx)

#         for ex in explodable:
#             if firstEx == number.index(str(ex).replace(" ","")):
#                 firstExplodable = ex
#                 break
        
#         # print("EXPLODABLE: ",end="")
#         # print(firstExplodable)
#         return firstExplodable

#searches the number, if a [ exists with a net 4 ['s on the left, then it has potential to be an explodable pair
#if from the [ we found earlier, there is a bunch of characters, and then a ] without another [, the the values
# enclosed in these must be explodable
def findExplodable(number):
    for x in range(len(number)):
        test = ""
        
        leftNetBrackets = number[:x].count("[") - number[:x].count("]")
        if number[x] == "[" and number[x+1].isnumeric() and leftNetBrackets >= 4:            
            i = x
            test = number[x]
            while True:
                # print(test)
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


# find the first valid point of explosion as there could be identical pairs earlier that are not unexplodable
# this point is the search index, from here, we find the the explodable paie, replace it with 0 and complete the
# addition operations to the right and left as stated in the problem
def explode(number,explodable):
    # print("exploded:  "+str(explodable).replace(" ","")+"  ",end="")
    print("    exploded:",end="")
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
    
    # search right for the first instance of a number
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
    
    # search left for the first number
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
            
            # print(num)
            number = number[:i+1] + str(exA+int(num)) + number[x+1:]
            break

    print(number)

    return number

# find any two characters that are numeric, therefore must be >10
# yes i know this doesnt account for >99 but thats not rlly gonna ever happen with this problem
def findSplit(number):
    for x in range(len(number)-2):
        twoChar = number[x]+number[x+1]
        if twoChar.isnumeric():
            # print("SPLIT:      "+twoChar)
            return twoChar
    return None

# replace the found splittable number with its split version
def split(number,toSplit):
    # print("splitted:  "+toSplit+"     ",end="")
    print("    splitted:",end="")
    
    a = int(int(toSplit)/2)
    b = int(int(toSplit)/2+0.5)
    replacement = f"[{a},{b}]"
    
    number = number.replace(toSplit,replacement,1)

    print(number)
    return number

# in a loop, try to explode as many times as possible
# once cant explode anymore, try to split, if:
#  - if cant split, reduction is over
#  - if can split, split, then start over
def reduce(number):
    # print("Reducing           "+number)
    print("    Reducing: "+number)

    
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

# finds innermost pairs using the same method as the find explodable
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
                print(test)
                return test

# completes the magnitude calculations until the snailfish number is reduced to one number
def magnitude(number):
    while True:
        pair = findPair(number)

        temp = pair.replace("[","").replace("]","")
        temp = temp.split(",")
        A = int(temp[0])
        B = int(temp[1])

        num = 3*A + 2*B

        number = number.replace(pair,str(num))
        print(number)
        if number.isnumeric():
            return number

# read the numbers, set total to the first one, add the next one to total, reduce, then add again
# repeat until the end of list of numbers then do magnitude calculation
if __name__ == "__main__":
    numbers = readFile()

    total = numbers[0]
    for x in range(1,len(numbers)):
        print()
        print("  "+total + "\number+ " + numbers[x])
        total = add(total,numbers[x])
        total = reduce(total)

    print()
    print(total)

    print(magnitude(total))
    
