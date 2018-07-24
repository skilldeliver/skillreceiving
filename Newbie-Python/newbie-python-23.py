import pygame, sys, random
from pygame.locals import*

pygame.init()
displaysurf = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Dochoice")

black = (0, 0, 0)
white = (153, 102, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
purple = (168, 7, 190)

num = random.randint(1,2)

if num == 1:
    do = "Do it"
else:
    do = "Don't do it"

font1Obj = pygame.font.Font('freesansbold.ttf', 82)
text1SurfaceObj = font1Obj.render("Just", True, purple, black)
text1RectObj = text1SurfaceObj.get_rect()
text1RectObj.center = (300, 100)


fontObj = pygame.font.Font('freesansbold.ttf', 82)
textSurfaceObj = fontObj.render( do, True, purple, black)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (300, 200) 


while True:
    displaysurf.fill(white)
    displaysurf.blit(text1SurfaceObj, text1RectObj)
    displaysurf.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
    pygame.display.update()
