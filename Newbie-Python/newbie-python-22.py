import sys, pygame, random

pygame.init()
Display_surf = pygame.display.set_mode((600, 400))
pygame.set_caption("Dochoice")

while True:
    for event in pygame.event.get():
        if event.type == "QUIT" or (event.type == "KEYUP" and event.key == "K_ESCAPE"):
            pygame.quit()
            sys.exit()
        pygame.display.update()





