import pygame
from pygame.locals import *
import sys

pygame.init()

SURF = pygame.display.set_mode((1000, 700), pygame.RESIZABLE)
pygame.display.set_caption("Something")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    SURF.fill((255, 255, 255))
    pygame.display.update()
        