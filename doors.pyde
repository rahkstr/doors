def setup():
    size(500, 300)
    initGame()
    
def draw():
    # we don't need to animate anything
    pass
    
def mouseClicked():
    global correctDoor, gameOver
    if gameOver:
        if pointInRect(mouseX, mouseY, 175, 100, 150, 100):
            initGame()
    else:
        # door 0
        if pointInRect(mouseX, mouseY, 50, 50, 100, 200):
            if correctDoor == 0:
                money(50, 50)
            else:
                death(50, 50)
            gameOver = True
        # door 1
        if pointInRect(mouseX, mouseY, 200, 50, 100, 200):
            if correctDoor == 1:
                money(200, 50)
            else:
                death(200, 50)
            gameOver = True
        # door 2
        if pointInRect(mouseX, mouseY, 350, 50, 100, 200):
            if correctDoor == 2:
                money(350, 50)
            else:
                death(350, 50)
            gameOver = True
        if gameOver:
            newGameButton()

def initGame():
    global correctDoor, gameOver
    background(0)
    door(50, 50)
    door(200, 50)
    door(350, 50)
    gameOver = False
    correctDoor = int(random(3))
    
def door(x, y):
    noStroke()
    # panel
    fill(125, 80, 50)
    rect(x, y, 100, 200)
    # handle
    fill(70)
    ellipse(x + 80, y + 110, 15, 15)
    
def newGameButton():
    fill(255)
    rect(175, 100, 150, 100)
    fill(0)
    text("Click to play again!", 195, 150)

def money(x, y):
    fill(0, 100, 0)
    rect(x, y, 100, 200)

def death(x, y):
    fill(100, 0, 0)
    rect(x, y, 100, 200)
    
def pointInRect(pX, pY, rX, rY, rW, rH):
    return pX > rX and pX < rX + rW and pY > rY and pY < rY + rH
