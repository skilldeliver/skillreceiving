import pygame
import sys
import time
from pygame.locals import*

pygame.init()

display_surface = pygame.display.set_mode((1200, 720))
pygame.display.set_caption("Gamish")

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 255)
# Font things
fontObj = pygame.font.Font('freesansbold.ttf', 62)
textSurfaceObj = fontObj.render('Hello world!', False, blue, white)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (200, 150)

#Sound things
pygame.mixer.music.load('Oasis.mp3')
pygame.mixer.music.play(-1, 0.0)


while True:

    display_surface.fill(white)
    display_surface.blit(textSurfaceObj, textRectObj)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()
    pygame.display.update()
