# USED IMAGES:
#            Shuttle Image - http://clubpenguin.wikia.com/wiki/File:Beta_Team_Solar_System_Space_Shuttle.png 
#                            https://www.clker.com/clipart-satelite.html
#                            http://scribblenauts.wikia.com/wiki/File:Asteroid.png

import pygame
import time 
from pygame.locals import *
import sys
import locale
import random

locale.setlocale(locale.LC_ALL, '')
pygame.init()

SIZE = X, Y = (600, 750)
SURF = pygame.display.set_mode(SIZE)
FPS = 60
CLOCK = pygame.time.Clock()
pygame.display.set_caption("Spaceship")
white = (255, 255, 255)
purpleish = (80, 49, 81)

font = pygame.font.SysFont("Arial Black", 30)
start = time.time()

xShuttle = int(X / 2)
yShuttle = int(Y - 180)
speedXShuttle = 0
speedYShuttle = 0
xSatelite = int(X / 2)
ySatelite = -50
speedShuttle = 10

spaceshipRect = pygame.Rect(xShuttle, yShuttle, 140, 180)
sateliteRect = pygame.Rect(xSatelite, ySatelite, 75, 55)

stars1 = pygame.image.load("SpaceStars1.png")
stars2 = pygame.image.load("SpaceStars2.png")
stars3 = pygame.image.load("SpaceStars3.png")
stars4 = pygame.image.load("SpaceStars4.png")
stars5 = pygame.image.load("SpaceStars5.png")
stars6 = pygame.image.load("SpaceStars6.png")
stars7 = pygame.image.load("SpaceStars7.png")
stars8 = pygame.image.load("SpaceStars8.png")
stars9 = pygame.image.load("SpaceStars9.png")
stars10 = pygame.image.load("SpaceStars10.png")
stars11 = pygame.image.load("SpaceStars11.png")
stars12 = pygame.image.load("SpaceStars12.png")
spaceship = pygame.image.load("Beta_Team_Solar_System_Space_Shuttle.png")
satelite = pygame.image.load("satelite-hi.png")

spaceship = pygame.transform.scale(spaceship, (140, 180))
satelite = pygame.transform.scale(satelite, (75, 55))


starsList = [stars1, stars2, stars3, stars4, stars5, stars6, stars7, stars8, stars9, stars10, stars11, stars12]
for i in starsList:
    i = pygame.transform.scale(i, SIZE)

temp = 0
num = 0
mins = 0
left = False
right = False

while 1:

    #if spaceshipRect.colliderect(sateliteRect) == 1: break

    text = font.render("{0:n}".format(temp) + " km", True, white)
    # Refreshing background images
    temp += 1
    if temp % 3 == 0:
        num += 1
        if num > 11:
            num = 0

    # Events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                left = True
                right = False
            if event.key == K_d or event.key == K_RIGHT:
                right = True
                left = False
        if event.type == KEYUP:
            if event.key == K_a or event.key == K_LEFT:
                left = False
            if event.key == K_d or event.key == K_RIGHT:
                right = False

    if left and spaceshipRect.left > 0:
        print("in")
        spaceshipRect.left -= speedShuttle
    if right and spaceshipRect.right < X:
        print("in")
        spaceshipRect.right += speedShuttle

    SURF.blit(starsList[int(num / 2)], (0, 0))
    SURF.blit(spaceship, sateliteRect)
    SURF.blit(satelite, sateliteRect)
    SURF.blit(text, (0, 0))
    CLOCK.tick(FPS)
    pygame.display.update()
    


