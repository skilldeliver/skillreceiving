import pygame
from pygame.locals import *

pygame.init()

DISP = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Something")
DISP.fill((0, 0, 255))
CANVAS = pygame.Surface((300, 300))
CANVAS.fill((255, 0, 0))

brush = pygame.image.load("brush.png")

while 1:
    x, y = pygame.mouse.get_pos()
    for e in pygame.event.get():
        if e.type == QUIT: raise SystemExit

    CANVAS.blit(brush, (x, y))
    pygame.display.flip()

