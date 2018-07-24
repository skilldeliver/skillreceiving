import pygame
from random import randint, choice
from pygame.locals import *
import string

max_lines = 100


class textblock():
    """ A block including one character """
    def __init__(self, character, font, background, fadetime, x_pos, y_pos):
        # Draw our character to the screen
        self.character = character
        self.font = font
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.cur_color = 0
        self.rect = None
        self.color_prog = [(255, 255, 255),
                           (250, 250, 250),
                           (150, 150, 150),
                           (125, 250, 125),
                           (0, 250, 0),
                           (0, 250, 0),
                           (0, 250, 0),
                           (0, 250, 0),
                           (0, 125, 0),
                           (0, 100, 0),
                           (0, 0, 0)]

        self.last_update = pygame.time.get_ticks()
        self.fade_interval = (fadetime * 1000)/len(self.color_prog)
        self.update(background)

    def update(self, background):
        # Update the character and redraw
        # When faded we return False, otherwise return True
        current_time = pygame.time.get_ticks()
        if (current_time - self.last_update) > self.fade_interval:
            self.last_update = current_time
            self.cur_color = self.cur_color + 1

            # In the matrix, randomly an individual character will
            # change, this helps us handle that situation
            if randint(0, 1000) == 1:
                self.character = choice(string.ascii_lowercase)

            if self.cur_color >= len(self.color_prog):
                background.fill(pygame.Color("black"), self.rect)
                return False

            text = self.font.render(self.character,
                                    1, self.color_prog[self.cur_color])
            textpos = text.get_rect()
            textpos.x = self.x_pos
            textpos.y = self.y_pos
            background.blit(text, textpos)
            self.rect = textpos
        return True


class textline():
    """ A line of text travelling down the screen """
    def __init__(self, font, background, x_pos, speed):
        self.x_pos = x_pos
        self.font = font
        self.speed = speed
        self.chars = []
        self.fade_time = randint(1, 4)
        self.head_y_pos = 0
        self.last_update = pygame.time.get_ticks()
        self.font_height = font.get_height()

        self.update(background)

    def update(self, background):
        to_remove = []
        for i in range(0, len(self.chars)):
            response = self.chars[i].update(background)
            if not response:
                to_remove.append(i)

        # We have to reverse sort the keys to remove, so we don't
        # mess up the indexes in the event we're deleting multiple items
        for i in sorted(to_remove, reverse=True):
            del(self.chars[i])

        current_time = pygame.time.get_ticks()
        if (current_time - self.last_update) > self.speed:
            self.last_update = current_time

            if self.head_y_pos < background.get_height():
                new_char = choice(string.ascii_lowercase)
                self.chars.append(textblock(new_char, self.font,
                                            background, self.fade_time,
                                            self.x_pos, self.head_y_pos))
                self.head_y_pos = self.head_y_pos + self.font_height
                return True

            if len(self.chars) == 0:
                return False
        return True


def add_line(matrix_lines, font, background):
    screen_width = background.get_width()/10
    matrix_lines.append(textline(font, background,
                                 randint(0, screen_width)*10,
                                 randint(30, 150)))


def main():

        # Initialise screen fullscreen
        pygame.init()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption('Falling Text')

        # Fill background
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))

        # Create our clock (locking to 60FPS)
        clock = pygame.time.Clock()

        # Draw our lines
        font = pygame.font.Font("resources/fonts/matrix.ttf", 24)

        matrix_lines = list()
        for i in range(10):
            add_line(matrix_lines, font, background)

        # Blit everything to the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)

        # Event loop
        while 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                if event.type == pygame.KEYDOWN:
                    return

            to_remove = []
            for i in range(0, len(matrix_lines)):
                response = matrix_lines[i].update(background)
                if not response:
                    to_remove.append(i)

            for i in to_remove:
                del(matrix_lines[i])
                add_line(matrix_lines, font, background)

            if len(matrix_lines) < max_lines:
                if randint(0, 10) > 8:
                    add_line(matrix_lines, font, background)

            screen.blit(background, (0, 0))
            pygame.display.flip()
            clock.tick(60)
            


if __name__ == '__main__':
    main()