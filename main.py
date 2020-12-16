import pgzrun

RED = 150,0,0
GREEN = 0,128,0
bg = GREEN

WIDTH = 800
HEIGHT = 600

SPEED=5
alienek = Actor('alien')
alien = Actor('alien')
alien.pos=400,300
alienek.pos=400,100

def draw():
    screen.fill(bg)
    alien.draw()
    alienek.draw()




def moveright():
    alien.left += SPEED
    if alien.left > WIDTH:
        alien.right = 0

    alienek.right -= SPEED
    if alienek.right > WIDTH:
        alienek.left = 0

def moveleft():
    alien.right -= SPEED
    if alien.right > WIDTH:
        alien.left = 0

    alienek.left += SPEED
    if alienek.left > WIDTH:
        alienek.right = 0

# def on_mouse_down():
#     global bg
#     bg=RED
#
# def on_mouse_up():
#     global SPEED
#     SPEED=SPEED+5

def on_key_down(key):
    if key==keys.LEFT:
        moveleft()
    if key==keys.RIGHT:
        moveright()
    if key==keys.ESCAPE:
        exit()

def on_key_up(key):
    if key==keys.SPACE:
        print('space up')

pgzrun.go()