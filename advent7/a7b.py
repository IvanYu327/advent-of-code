import numpy

arr = numpy.array([])

with open('advent7/info.txt') as f:
    for readline in f:
        arr = [int(numeric_string) for numeric_string in readline.strip().split(",")]
        
  
print(numpy.sum(arr))
print(numpy.average(arr))
print(numpy.median(arr))

bestPos = 0
lowestFuel = 0;

for pos in range(2000):
    fuel = 0;
    for crab in arr:
        for x in range(abs(crab - pos)+1):         
            fuel += x
            if lowestFuel != 0 and fuel > lowestFuel:
                break
    
    if lowestFuel == 0 or fuel < lowestFuel:
        lowestFuel = fuel
        print(f"{pos}: {fuel}")
    
