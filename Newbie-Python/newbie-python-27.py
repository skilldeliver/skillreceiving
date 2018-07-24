import pygame, sys
from pygame.locals import *


pygame.init()
w = 640
h = 480
surf = pygame.display.set_mode((w, h))
pygame.display.set_caption("Smth")
aqua = (2, 255, 176)

while True:
    surf.fill(aqua)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
