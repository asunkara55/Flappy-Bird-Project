import pygame
import time
import random
import math

# Window size
windowX = 720*1.5
windowY = 480

# defining colors
black = pygame.Color(0, 0, 0)
gray = pygame.Color(35, 35, 35)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
headColor = pygame.Color(50, 190, 130)

# Initialising pygame
pygame.init()

fps = 35

# Initialise game window
pygame.display.set_caption('The Better Flappy Bird Game')  # Title
game_window = pygame.display.set_mode((windowX, windowY))


birdSize = (40,40)
FlappyBirdUser = pygame.image.load('FlappyBird.png')  # Flappy Bird animal
FlappyBirdUser = pygame.transform.scale(FlappyBirdUser, birdSize)


FlappyBirdBackground = pygame.image.load('FlappyBirdBackground.png')  # Background
FlappyBirdBackground = pygame.transform.scale(FlappyBirdBackground, (FlappyBirdBackground.get_width()*(windowY/FlappyBirdBackground.get_height()), windowY)).convert()
bgwidth = FlappyBirdBackground.get_width()


FlappyBirdPole = pygame.image.load('pipe_5.png')  # poles
polewidth = 60
FlappyBirdPole = pygame.transform.scale(FlappyBirdPole, (polewidth, FlappyBirdPole.get_height()*polewidth/FlappyBirdPole.get_width()))
poleHeight = FlappyBirdPole.get_height()

UpsideDownPole = pygame.transform.flip(FlappyBirdPole, False, True)

scroll = 0
tilesCount = math.ceil((windowX / bgwidth + 1))
print(tilesCount)

clock = pygame.time.Clock()
scrollDistance = 5

def DrawBird (y):
    game_window.blit(FlappyBirdUser, (windowX/3, y))


pipeGap = 90
pipespacing = 200
def drawpole (x,y):
    game_window.blit(FlappyBirdPole, (x,y))
    game_window.blit(UpsideDownPole, (x,y-pipeGap-UpsideDownPole.get_height()))


def drawallpoles (poleList):
    for cords in poleList:
        drawpole(cords.x, cords.y)

def ScrollPoles():
    global poleList
    global DistanceFromLastPole
    DistanceFromLastPole += scrollDistance
    for cords in poleList:
        cords.x -= scrollDistance
        if cords.x < 0-polewidth:
            poleList.remove(cords)


floorHeight = int(windowY*0.735)

DistanceFromLastPole = pipespacing
def AddPole():
    global poleList
    global DistanceFromLastPole
    print(DistanceFromLastPole)
    if DistanceFromLastPole >= pipespacing:
        pipeYPosition = random.randint(pipeGap+30, floorHeight-30)
        poleList.append(Pole(windowX, pipeYPosition))
        DistanceFromLastPole = -polewidth




class Pole:
    def __init__(self, x, y):
        self.x = x
        self.y = y


poleList = []
AddPole()
birdHeight = windowY/2

velocity = 0
direction = "down"
def MoveBird():
    global velocity
    global birdHeight
    global floorHeight
    global direction

    if direction == "up":
        velocity = -10  # Jump height
        direction = "down"
    else:
        velocity += 2  # Downward acceleration

    birdHeight += velocity



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                quit()
            if event.key == pygame.K_SPACE:
                direction = "up"



    for a in range (0,tilesCount):
        game_window.blit(FlappyBirdBackground, (a * bgwidth + scroll, 0))

    #scroll background
    scroll -= scrollDistance

    #scroll reset
    if abs(scroll) > bgwidth:
        scroll = 0
    ScrollPoles()
    AddPole()
    drawallpoles(poleList)


    MoveBird()
    DrawBird(birdHeight)
    #print("tick " + str(pygame.time.get_ticks()))







    pygame.display.flip()
    clock.tick(fps)
