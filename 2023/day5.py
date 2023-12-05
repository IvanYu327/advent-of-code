from utils import get_input

# INPUT PARSING

input = get_input()
maps = {}


seeds = input[0].replace("seeds: ","").split(" ")
seeds = list(map(int, seeds))

map_name = ""
for line in input[1:]:
    if not line:
        continue

    if not line[0].isnumeric():
        map_name = line.replace(" map:", "")
        maps.update({map_name: []})
    else:
        data = line.split(" ")
        maps[map_name].append({
            "destination": int(data[0]),
            "source": int(data[1]),
            "range": int(data[2]),
        })

# PART 1

best_seed = 0
lowest_location = float("inf")

for seed in seeds:
    current = seed
    for map_name in maps.keys():
        for map in maps[map_name]:
            source = map["source"]
            destination = map["destination"]
            range = map["range"]

            if current >= source and current <= source + range:
                current -= source - destination
                break

    if current < lowest_location:
        lowest_location = current
        best_seed = seed
    
print(lowest_location)


# PART 2
