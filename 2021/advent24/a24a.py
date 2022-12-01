def readFile():
    instructions = []

    with open('advent24/info.txt') as f:
        for readline in f:
            x = readline.strip()
            if x != "inp w":
                x = x.replace(" ","")
                x = x[1] + x[0] + x[2:]

            instructions.append(x)

    return instructions

def check(num,instructions):
    num = str(num)

    w = 0
    x = 0
    y = 0 
    z = 0

    for step in instructions:
        if step[0] == "inp":
            w = num[0]
            num = num[1:]
        
        else:
            


            
            if step[0] == "w":
                w = eval(step)
            elif step[0] == "x":
                x = eval(step)
            elif step[0] == "y":
                y = eval(step)
            elif step[0] == "z":
                z = eval(step)



            # term1 = 0
            # if step[1] == "w":
            #     term1 = w
            # elif step[1] == "x":
            #     term1 = x
            # elif step[1] == "y":
            #     term1 = y
            # elif step[1] == "z":
            #     term1 = z

            # if step[2].isnumeric():
            #     term2 = int(step[2])
            # elif step[2] == "w":
            #     term1 = w
            # elif step[2] == "x":
            #     term1 = x
            # elif step[2] == "y":
            #     term1 = y
            # elif step[2] == "z":
            #     term1 = z
            
            # if step[0] == "mul":
            #     term1 = term1 * term2
            # elif step[0] == "add":
            #     term1 = term1 + term2
            # elif step[0] == "mod":
            #     term1 = term1 % term2
            # elif step[0] == "div":
            #     term1 = term1 / term2
            
            # if step[1] == "w":
            #     w = term1
            # elif step[1] == "x":
            #     x = term1
            # elif step[1] == "y":
            #     y = term1
            # elif step[1] == "z":
            #     z = term1


    return z

if __name__ == "__main__":
    instructions = readFile()

    for x in range(14):
        print(instructions[x*18:(x+1)*18])
    
    print(check(11111111111111,instructions))