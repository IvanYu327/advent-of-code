from utils import get_input
from math import sqrt
data = get_input(8, strip=True)

coords = []
for line in data:
    c = line.split(',')
    c = tuple([int(num) for num in c])
    coords.append(c)

def distance(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

n = len(coords)

# Build pairs
pairs = []
for i in range(n):
    for j in range(i+1, n):
        pairs.append((i, j, distance(coords[i], coords[j])))

pairs.sort(key = lambda x : x[2])

# union find
parent = list(range(n))
size = [1] * n


def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False
    if size[ra] < size[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True

# run for K successful unions
K = 1000

for idx in range(K):
    a, b, _ = pairs[idx]
    union(a, b) 

# collect component sizes
components = {}
for i in range(n):
    r = find(i)
    components.setdefault(r, 0)
    components[r] += 1

sizes = sorted(components.values(), reverse=True)
answer = sizes[0] * sizes[1] * sizes[2]
print("Part 1:", answer)

# Part 2

# run for K successful unions
idx = 0
sizes = [0,0]
res = 0

for i in range(len(pairs)):
    a, b, _ = pairs[i]
    union(a, b)

    # collect component sizes
    components = {}
    for i in range(n):
        r = find(i)
        components.setdefault(r, 0)
        components[r] += 1

    sizes = sorted(components.values(), reverse=True)
    if len(sizes) == 1:
        res = coords[a][0] * coords[b][0]
        break

print("Part 2:", res)