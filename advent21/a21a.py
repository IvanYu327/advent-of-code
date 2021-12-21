if __name__ == "__main__":
    pos = [10,3]
    scores = [0,0]

    die = 1
    rollCount = 0
    p = 1

    while True:
        if p == 1:
            p = 0
        else:
            p = 1
        
        for x in range(3):
            pos[p] += die

            die += 1
            if die == 101:
                die = 1
        
        rollCount+= 3
        
        pos[p] = pos[p]%10
        if pos[p] == 0:
            pos[p] = 10

        scores[p] += pos[p]

        if max(scores) >= 1000:
            break

    print(min(scores),rollCount)
    print(min(scores)*rollCount)    