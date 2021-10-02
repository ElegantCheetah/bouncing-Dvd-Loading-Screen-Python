import pygame
from time import sleep
from random import randint
from pygame.locals import *

pygame.init()

xEdge,yEdge = 650, 900

screen = pygame.display.set_mode((xEdge,yEdge), vsync = 1)
logo = 'logo.png'

myimage = pygame.image.load(logo)
imagerect = myimage.get_rect()

#start pos
x = 100
y = 100
speedX = 5
speedY = 5
sizeX,sizeY =  100, 100
def logic():
    global x,y,startEdge,endEdge,sizeX,sizeY,speedX,speedY
    
    screen.blit(myimage,(x,y))

    x+=speedX
    y+=speedY
    
    #speedX and Y random values
    randomValue = 50

    if x > xEdge-sizeX-100:
        speedX = -randomValue
    if x < 0:
        speedX = randomValue
    if y > yEdge-sizeY-100:
        speedY = -randomValue
    if y < 0:
        speedY = randomValue

    print("X: ",x,"Y: ",y,"SpeedX: ",speedX,"SpeedY: ",speedY, 'xEdge: ', xEdge, 'yEdge: ', yEdge)

#gameloop
while True:
    sleep(1/60)#60 fps
    screen.fill((0,0,0))
    logic()
    pygame.display.flip()