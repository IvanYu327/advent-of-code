# Not a solution, i solved it by hand, this just calculated the move costs

    #############
    #...........#
    ###D#B#C#C###
      #D#A#B#A#
      #########

def readFile():
    file = "advent23/part1.txt"
    file = "advent23/part2.txt"


    total = 0

    with open(file) as f:
        for readline in f:
            step = readline.strip()
            amph = step[0]
            if len(step) > 2:
                steps = int(step[1:3])
            else:
                steps = int(step[1])
            
            if amph == "a":
                total += steps * 1
            elif amph == "b":
                total += steps * 10
            elif amph == "c":
                total += steps * 100
            elif amph == "d":
                total += steps * 1000
    
    
    return total


if __name__ == "__main__":
    print(readFile())