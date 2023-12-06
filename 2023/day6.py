test_races = [(7,9) , (15,40) , (30,200)]
races = [(47,400) , (98,1213) , (66,1011) , (98,1540)]

# PART 1

total = 1

for race in races:
    time = race[0]
    record = race[1]

    ways_beaten = 0

    for x in range(1, time):
        if x * (time - x) > record:
            ways_beaten += 1
    
    total *= ways_beaten

print(total)



# PART 2

races = [(47986698,400121310111540)]
total = 1

for race in races:
    time = race[0]
    record = race[1]

    ways_beaten = 0

    for x in range(1, time):
        if x * (time - x) > record:
            ways_beaten += 1
    
    total *= ways_beaten

print(total)

