import numpy as np

if __name__ == "__main__":
    players = [10,3]
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
            players[p] += die

            die += 1
            if die == 101:
                die = 1
        
        rollCount+= 3
        
        players[p] = players[p]%10
        if players[p] == 0:
            players[p] = 10

        scores[p] += players[p]

        if max(scores) >= 1000:
            break

    print(min(scores),rollCount)
    print(min(scores)*rollCount)    