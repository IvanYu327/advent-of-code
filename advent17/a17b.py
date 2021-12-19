tx = [143,177]
ty = [-106,-71]

# tx = [20,30]
# ty = [-10,-5]

def launch(xv,yv):
    xPos = 0
    yPos = 0

    while True:
        
        xPos += xv
        yPos += yv
        if xv != 0:
            xv -= 1
        yv-=1

        if xPos >= tx[0] and xPos <= tx[1] and yPos >= ty[0] and yPos <= ty[1]:
            return 1
        elif xPos > tx[1] or yPos < ty[0]:
            return 0

if __name__ == "__main__":
    
    heights = 0
    for xV in range(0,tx[1]+1):
        for yV in range(ty[0],500):
            print(xV,yV)
            heights += launch(xV,yV)
    
    print(heights)









