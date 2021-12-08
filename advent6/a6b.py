import numpy as np
array = np.array([3,5,1,5,3,2,1,3,4,2,5,1,3,3,2,5,1,3,1,5,5,1,1,1,2,4,1,4,5,2,1,2,4,3,1,2,3,4,3,4,4,5,1,1,1,1,5,5,3,4,4,4,5,3,4,1,4,3,3,2,1,1,3,3,3,2,1,3,5,2,3,4,2,5,4,5,4,4,2,2,3,3,3,3,5,4,2,3,1,2,1,1,2,2,5,1,1,4,1,5,3,2,1,4,1,5,1,4,5,2,1,1,1,4,5,4,2,4,5,4,2,4,4,1,1,2,2,1,1,2,3,3,2,5,2,1,1,2,1,1,1,3,2,3,1,5,4,5,3,3,2,1,1,1,3,5,1,1,4,4,5,4,3,3,3,3,2,4,5,2,1,1,1,4,2,4,2,2,5,5,5,4,1,1,5,1,5,2,1,3,3,2,5,2,1,2,4,3,3,1,5,4,1,1,1,4,2,5,5,4,4,3,4,3,1,5,5,2,5,4,2,3,4,1,1,4,4,3,4,1,3,4,1,1,4,3,2,2,5,3,1,4,4,4,1,3,4,3,1,5,3,3,5,5,4,4,1,2,4,2,2,3,1,1,4,5,3,1,1,1,1,3,5,4,1,1,2,1,1,2,1,2,3,1,1,3,2,2,5,5,1,5,5,1,4,4,3,5,4,4])
# arr = np.array([3,4,3,1,2])

mult = np.array([])
for x in range(6):
    mult = np.append(mult,(array == x).sum())

print(mult)
total = 0
days = 256

for x in range(1,6):
    arr = np.array([x])
    
    for day in range(int(days/2)):
    

        zeros = (arr <= 0).sum()
        arr[arr == 0] = 7
        new=np.full((1, zeros), 9)
        arr = np.append(arr,new)
        arr = arr - 1

    print(arr) 
   
    multt = np.array([])
    for z in range(9):
        multt = np.append(multt,(arr == z).sum())
    
    print(x, multt)
    totall = 0

    for y in range(9):
        arrr = np.array([y])
        
        for dayy in range(int(days/2)):
        

            zeross = (arrr <= 0).sum()
            arrr[arrr == 0] = 7
            new=np.full((1, zeross), 9)
            arrr = np.append(arrr,new)
            arrr = arrr - 1
        
        totall+=len(arrr)*multt[y]
   
    total+=totall*mult[x]

            
print(total)