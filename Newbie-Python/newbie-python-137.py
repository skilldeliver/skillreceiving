        import pygame as pg
        from pygame.locals import *


        pg.init() 

        keys = []

        disp = pg.display.set_mode((1, 1))
        loop = 1
        while loop:
            for e in  pg.event.get():
                print(e)
                if e.type == KEYDOWN:
                    if e.key == K_SPACE:
                        loop = 0
                    keys.append(str(e.key))

            pg.display.update()


        pg.quit()
        for i in keys:
            print(chr(int(i)))
