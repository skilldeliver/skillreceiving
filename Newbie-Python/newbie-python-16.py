import pygame
import sys
from pygame.locals import*

pygame.init()

fps = 30
fpsClock= pygame.time.Clock()

display_surface = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Game")
white = (255, 255, 255)
catimg = pygame.image.load(C:\Users\HP\source\repos\PythonApplication16\PythonApplication16\cat.png)
catx = 10
caty = 10
direction = 'right'



while True:
    display_surface.fill(white)

    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'up'
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'

    display_surface.blit(catimg,(catx, caty))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(fps)

