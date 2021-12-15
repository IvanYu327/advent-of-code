from collections import Counter

def readFile():
    file = "advent14/test.txt"
    # file = "advent14/info.txt"

    polymer = ""
    templates=[]

    with open(file) as f:
        for readline in f:
            if polymer == "":
                polymer = readline.strip()
            
            elif readline.strip() != "":
                temp = readline.strip().split(" -> ")
                templates.append([temp[0],temp[1]])
    
    return polymer,templates

def solve(polymer,templates):
    for step in range (1,11):
        for x in range(len(polymer)-2,-1,-1):
            for template in templates:
                if polymer[x]+polymer[x+1] == template[0]: 
                    polymer = polymer[:x+1]+template[1]+polymer[x+1:]
                    break
        
        print(step)

    most = Counter(polymer).most_common()[0]
    least = Counter(polymer).most_common()[:-2:-1] 

    print(most)
    print(least)
    print(most[1]-least[0][1])

if __name__ == "__main__":
    polymer = readFile()[0]
    templates = readFile()[1]
    solve(polymer,templates)