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

arr = []

def decode(string):
    versionTotal = 0

    while string != "" and int(string,2) != 0:
        version = int(string[:3],2)
        versionTotal += version
        string = string[3:]
        type = int(string[:3],2)
        string = string[3:]
        

        if type == 4:
            temp = ""
            while True:        
                temp += string[1:5]
                
                if string[0] == "0":
                    string = string[5:]
                    break

                string = string[5:]            
            arr.append([version,type,int(temp,2)])
        else:
            if string[0] == "0":
                string = string[1:]
                length = string[:15]
                string = string[15:]
            else:
                string = string[1:]
                length = string[:11]
                string = string[11:]
            
            length = int(length,2)
            arr.append([version,type,length])
        print(arr)

    return versionTotal
            


        
        


if __name__ == "__main__":
    string = readFile()
    string = toBin(string)
    print(decode(string))
    