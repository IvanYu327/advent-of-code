import numpy as np
import re

arr = []

with open('2022/advent/input.txt', "r") as f:
    for readline in f: 
        line = re.split(r",| ", readline.strip())
        # line = list(map(int, line))
        arr.append(line)

# PART 1



# PART 2