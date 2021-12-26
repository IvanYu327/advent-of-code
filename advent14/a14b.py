from copy import deepcopy

polymer = "SHHBNFBCKNHCNOSHHVFF"
templates = {}
pairs = {}
letterCounts = {}

file = "advent14/info.txt"

with open(file) as f:
    for readline in f:       
        temp = readline.strip().split(" -> ")
        templates[temp[0]] = temp[1]

for x in range(len(polymer)-1):
    if polymer[x] in letterCounts:
        letterCounts[polymer[x]] += 1
    else:
        letterCounts[polymer[x]] = 1
    
    pair = polymer[x:x+2]
    if pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1

if polymer[-1] in letterCounts:
    letterCounts[polymer[-1]] += 1
else:
    letterCounts[polymer[-1]] = 1

print(polymer)
print(pairs)
print(letterCounts)
print(templates)

# steps = 10
steps = 40
for x in range (steps):
    print(f"after step: {x+1}")
    nextStepPairs = deepcopy(pairs)
    
    for key in pairs:
        # print("test 1")
        # print(pairs)
        insertion = templates[key] 
        
        newPair1 = key[0] + insertion
        newPair2 = insertion + key[1]

        count = pairs[key]
        
        nextStepPairs[key] -= count

        if newPair1 in nextStepPairs:
            nextStepPairs[newPair1] += count
        else:
            nextStepPairs[newPair1] = count

        if newPair2 in nextStepPairs:
            nextStepPairs[newPair2] += count
        else:
            nextStepPairs[newPair2] = count

        if insertion in letterCounts:
            letterCounts[insertion] += count
        else:
            letterCounts[insertion] = count
        
        # print(key, insertion, newPair1, newPair2, count)
        # print(pairs)
    
    pairs = nextStepPairs

    print(pairs)
    print(letterCounts)

counts = []    
for key in letterCounts:
    if letterCounts != 0:
        counts.append(letterCounts[key])

print(max(counts) - min(counts))