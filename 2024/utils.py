def get_input(day):
    arr = []
    with open(f'2024/input{day}.txt', "r") as f:
        for readline in f:         
            arr.append(readline.strip())

    return arr
