def get_input():
    arr = []
    with open('2023/input.txt', "r") as f:
        for readline in f:         
            arr.append(readline.strip())

    return arr
