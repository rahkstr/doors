def setup():
    global correctDoor, gameOver
    size(500, 300)
    background(0)
    door(50, 50)
    door(200, 50)
    door(350, 50)
    gameOver = False
    correctDoor = int(random(3))
    
def draw():
    # we don't need to animate anything
    pass
    
def mouseClicked():
    global correctDoor, gameOver
    if not gameOver:
        # door 0
        if mouseX > 50 and mouseX < 150 and mouseY > 50 and mouseY < 250:
            if correctDoor == 0:
                money(50, 50)
            else:
                death(50, 50)
            gameOver = True
        # door 1
        if mouseX > 200 and mouseX < 300 and mouseY > 50 and mouseY < 250:
            if correctDoor == 1:
                money(200, 50)
            else:
                death(200, 50)
            gameOver = True
        # door 2
        if mouseX > 350 and mouseX < 450 and mouseY > 50 and mouseY < 250:
            if correctDoor == 2:
                money(350, 50)
            else:
                death(350, 50)
            gameOver = True
    
def door(x, y):
    noStroke()
    # panel
    fill(125, 80, 50)
    rect(x, y, 100, 200)
    # handle
    fill(70)
    ellipse(x + 80, y + 110, 15, 15)

def money(x, y):
    fill(0, 100, 0)
    rect(x, y, 100, 200)

def death(x, y):
    fill(100, 0, 0)
    rect(x, y, 100, 200)
