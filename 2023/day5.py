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
            _range = map["range"]

            if current >= source and current <= source + _range:
                current -= source - destination
                break

    if current < lowest_location:
        lowest_location = current
        best_seed = seed
    
print(lowest_location)


# PART 2
ranges = []
for i in range(0, len(seeds), 2):
    ranges.append((seeds[i], seeds[i]+seeds[i+1] - 1))

best_seed = 0


for map_name in maps.keys():
    print("new map:", ranges)
    new_ranges = []
    
    for range in ranges:
        current_ranges = [range]
        start = range[0]
        end = range[1]


        for map in maps[map_name]:
            print(map)
            if not current_ranges:
                break

            current_range = current_ranges.pop()
            
            source = map["source"]
            destination = map["destination"]
            r = map["range"] - 1
            change = destination - source
            # print(source, start, end, source + r)
            if source <= start <= end <= source + r:
                # print("within")
                new_ranges.append((start+change, end+change))

            elif start <= source <= end <= source + r:
                new_ranges.append((source+change, end+change))
                current_ranges.append((start, source-1))
            
            elif source <= start <= source + r <= end:
                new_ranges.append((start+change, source+r+change))
                current_ranges.append((source+r+1, end))
            
            elif start <= source <= source + r <= end:
                new_ranges.append((source+change, source+r+change))
                current_ranges.append((start, source-1))
                current_ranges.append((source+r+1, end))
            
            else:
                current_ranges.append(current_range)
            
            print(current_ranges)
    
        new_ranges += current_ranges
        print(new_ranges)
    
    ranges = new_ranges

print(ranges)
total = 0

lowest_location = float("inf")

for range in ranges:
    total += range[1] - range[0] + 1
    if range[0] < lowest_location:
        lowest_location = range[0]

print(total)
print(lowest_location)


