import pygame
from time import sleep
from random import randint


pygame.init()

xEdge,yEdge = 1800, 800

screen = pygame.display.set_mode((xEdge,yEdge), vsync = 1)
logo = 'logo.png'

myimage = pygame.image.load(logo)
imagerect = myimage.get_rect()

#start pos
x = 100
y = 100
speedX = 5 #randint(1,5)#first randomed then get new random values
speedY = 5 #randint(1,5) 
sizeX,sizeY =  100, 100
def logic():
    global x,y,startEdge,endEdge,sizeX,sizeY,speedX,speedY
    
    screen.blit(myimage,(x,y))

    x+=speedX
    y+=speedY
    
    #speedX and Y random values
    randomValue = randint(1,5)

    if x > xEdge-sizeX:
        speedX = -randomValue
    if x < 0:
        speedX = randomValue
    if y > yEdge-sizeY:
        speedY = -randomValue
    if y < 0:
        speedY = randomValue

    print("X: ",x,"Y: ",y,"SpeedX: ",speedX,"SpeedY: ",speedY, 'xEdge: ', xEdge, 'yEdge: ', yEdge)

#gameloop
while True:
    sleep(1/60)#30 fps
    screen.fill((0,0,0))
    logic()
    pygame.display.flip()




