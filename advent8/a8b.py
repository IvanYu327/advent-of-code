arr = []

with open('advent8/info.txt') as f:
    for readline in f:
        arr.append(readline.strip())


total = 0

for entry in arr:
    decoder = [ "" for i in range(10) ]
    signal = entry.split("|")[0].split(" ")
    output = entry.split("|")[1].split(" ")

    signal.pop(signal.index(''))
    output.pop(output.index(''))

    for x in signal:
        signal[signal.index(x)] = "".join(sorted(x))

    for x in output:
        output[output.index(x)] = "".join(sorted(x))

    for x in signal:
        if(len(x)) == 2:
            decoder[1] = x
        elif(len(x)) == 3:
            decoder[7] = x
        elif(len(x)) == 4:
            decoder[4] = x
        elif(len(x)) == 7:
            decoder[8] = x

    for x in [1,4,7,8]:
        signal.pop(signal.index(decoder[x]))

    for x in signal:
        if len(x) == 6:
            if decoder[7][0] in x and decoder[7][1] in x and decoder[7][2] in x: #only 9 and 0 have 6 lines and contain the lines of 7
                if decoder[4][0] in x and decoder[4][1] in x and decoder[4][2] in x and decoder[4][3] in x: #out of 9 and 0, only 9 will contain all lines in 4
                    decoder[9] = x
                else:
                    decoder[0] = x

    for x in [0,9]:
        signal.pop(signal.index(decoder[x]))

    for x in signal:
        if len(x) == 6:
            decoder[6] = x
            signal.pop(signal.index(x))

    #Now only the 5 line digits are left, 2,3,5
    for x in signal:
        if decoder[1][0] in x and decoder[1][1] in x: #only 3 contains all lines that make up 1
            decoder[3] = x
            signal.pop(signal.index(x))

    for x in signal:
        if x[0] in decoder[6] and x[1] in decoder[6] and x[2] in decoder[6] and x[3] in decoder[6] and x[4] in decoder[6]: 
            # if this signal's lines are all in the lines of 6, this must be 5, not 2
            decoder[5] = x
            signal.pop(signal.index(x))

    decoder[2] = signal[0]

    for digit in output:
        for x in decoder:
            if digit == x:
                output[output.index(digit)] = decoder.index(x)

    num = 0
    for x in range(4):
        num += int(output[x]) * ( 10 ** (3-x))

    total += num

print(total)