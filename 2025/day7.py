from utils import get_input
data = get_input(7, strip=True)

grid = []


# Part 1
n = len(data[0])
start = data[0].index('S')

beams = [0] * n
beams[start] = 1

splits = 0
for line in data[1:]:
    next_beams = [0] * n
    for pos, val in enumerate(beams):
        if val == 0:
            continue
        
        if line[pos] == '^':
            splits += 1
            if pos+1 < n:
                next_beams[pos+1] += val
            if pos-1 >= 0:
                next_beams[pos-1] += val
        elif line[pos] == '.':
            next_beams[pos] += val

    
    beams = next_beams

print("Part 1:", splits)
print("Part 2:", sum(next_beams))