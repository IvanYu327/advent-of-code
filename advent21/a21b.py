

def winCombinations(a,pos,score,step):
    if step %3 == 0:
        score+pos

    pos = pos%10
    if pos == 0:
        pos = 10
    
    if score >= 21:
        return step
    else:
        a = a + winCombinations(a,pos+1,score,step+1)
        a = a + winCombinations(a,pos+2,score,step+1)
        a = a + winCombinations(a,pos+3,score,step+1)
        return a




if __name__ == "__main__":

    combo1 = []
    winCombinations(combo1,4,0,0)
    print(len(combo1))