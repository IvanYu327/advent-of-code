import numpy as np

def readFile():
    file = "advent16/info.txt"

    string = ""

    with open(file) as f:
        for readline in f:
            string += readline
    
    return string

def toBin(inp):
    string = ""
    for s in inp:
        int_value = int(s, 16)
        bin_value = str(bin(int_value))[2:].zfill(4)
        string += bin_value
    
    return string



def decode(string):
    versionTotal = 0
    arr = []
    while string != "" and int(string,2) != 0:
        version = int(string[:3],2)
        versionTotal += version
        string = string[3:]
        type = int(string[:3],2)
        string = string[3:]
        
        bits = 6

        if type == 0:
            type = "sum"
        elif type == 1:
            type = "product"
        elif type == 2:
            type = "min"
        elif type == 3:
            type = "max"
        elif type == 4:
            type = "value"
        elif type == 5:
            type = "greater"
        elif type == 6:
            type = "less"
        elif type == 7:
            type = "equal"  

        if type == "value":
            temp = ""
            while True:        
                temp += string[1:5]
                bits += 5
                if string[0] == "0":
                    string = string[5:]
                    break

                string = string[5:]            
            arr.append([bits,type,int(temp,2)])
        else:
            bits += 1


            if string[0] == "0":
                string = string[1:]
                bits += 15                
                count = "bits"

                length = string[:15]
                string = string[15:]

            else:
                string = string[1:]
                bits += 11
                count = "subs"

                length = string[:11]
                string = string[11:]
                
            length = int(length,2)
            arr.append([bits,type,length,count])

    return arr
            

def solve(arr):
    while len(arr) > 1:
        # print(arr)
        for i in range(len(arr)):
            if i > len(arr)-1:
                break

            packet = arr[i]
            if packet[1] != "value" and arr[i+1][1] == "value":
                
                temp = [packet]
                tempIndex = i+1
                
                # print(packet)
                if packet[3] == "bits":
                    bits = packet[2]
                    # print(bits)
                    while bits > 0:
                        # print(tempIndex,end=" ")
                        if arr[tempIndex][1] == "value":
                            temp.append(arr[tempIndex])
                            bits -= arr[tempIndex][0]
                            tempIndex+=1
                        else:
                            temp = []
                            break

                else: #subs
                    subs = packet[2]
                    # print(subs)
                    while subs > 0:
                        # print(tempIndex,end=" ")
                        if arr[tempIndex][1] == "value":
                            temp.append(arr[tempIndex])
                            tempIndex+=1
                            subs -=1
                        else:
                            temp = []
                            break
                
                if temp != []:    
                    print("=====OPERATING=====")
                    # print(len(temp)-1)
                    replace = operate(temp)
                    arr[i] = replace
                    for x in range(len(temp)-1):
                        arr.pop(i+1)
                    
                    # print()
                    break
                
    return str(arr[0][2])
                


def operate(temp):
    # print(temp)
    operator = temp[0][1]
    numbers = []

    bitCount = 0
    for x in temp:
        bitCount += x[0]

    for x in range(1,len(temp)):
        numbers.append(temp[x][2])
    
    
    value = 0

    if operator == "sum":
        value =  np.sum(numbers)
    elif operator == "product":
        x = 1
        for number in numbers:
            x*=number
        value = x
    elif operator == "min":
        value =  min(numbers)
    elif operator == "max":
        value =  max(numbers)
    elif operator == "greater" and len(numbers)==2:
        if numbers[0] > numbers [1]:
            value =  1
        else:
            value =  0
    elif operator == "less" and len(numbers)==2:
        if numbers[0] < numbers [1]:
            value =  1
        else:
            value =  0
    elif operator == "equal" and len(numbers)==2:
        if numbers[0] == numbers[1]:
            value =  1
        else:
            value =  0
    
    result = [bitCount, "value", value]
    print(temp[0],numbers," ==> ",result)
    if temp[0][3] == "bits":
        print(temp[0][2]+temp[0][0] == result[0])
    return result

if __name__ == "__main__":
    string = readFile()
    string = toBin(string)
    arr = decode(string)
    for line in arr:
        print(line)
    print("OOGA BOOGA: "+solve(arr))
    