def get_input(day, strip = True):
    arr = []
    with open(f'2025/input{day}.txt', "r") as f:
        for readline in f:
            readline.rstrip('\n')
            if strip:
                readline = readline.strip()
            arr.append(readline)

    return arr
