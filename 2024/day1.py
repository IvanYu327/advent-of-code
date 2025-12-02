from utils import get_input
from math import floor, ceil
input_data = get_input(1)

position = 50
pwd1 = 0
pwd2 = 0

for line in input_data:
    direction = 1 if line[0] == "R" else -1
    step = int(line[1:])
    
    start = position
    end = position + direction * step
    
    if position % 100 == 0:
        pwd1 += 1
    
    s_offset = direction if start % 100 == 0 else 0
    e_offset = direction if end % 100 == 0 else 0
    crossings = abs(floor((start + s_offset)/100) - floor((end + e_offset)/100))
    pwd2 += crossings

    position = end

print("pwd1: ", pwd1)
print("pwd2: ", pwd2)
