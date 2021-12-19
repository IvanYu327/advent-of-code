tx = [143,177]
ty = [-106,-71]

# tx = [20,30]
# ty = [-10,-5]

def launch(xv,inpYv):
    yv = inpYv
    xPos = 0
    yPos = 0

    maxYPos = 0

    while True:
        
        xPos += xv
        yPos += yv
        maxYPos = max(maxYPos,yPos)
        if xv != 0:
            xv -= 1
        yv-=1

        if xPos >= tx[0] and xPos <= tx[1] and yPos >= ty[0] and yPos <= ty[1]:
            return maxYPos
        elif xPos > tx[1] or yPos < ty[0]:
            return "missed"

if __name__ == "__main__":
    
    maxHeight = 0

    for xV in range(0,tx[1]):
        for yV in range(0,500):
            print(xV,yV)
            height = launch(xV,yV)
            if height != "missed":
                maxHeight = max(maxHeight,height)
    
    print(maxHeight)









