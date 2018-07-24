import pygame
import sys

from pygame.locals import *

pygame.init()

Display_Surface = pygame.display.set_mode((400, 300))

pygame.display.set_caption("Игра")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
			
			
