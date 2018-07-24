import pygame, pygame.font
import random


def IsWritten():
    defTemp = True
    for x in xrange((lettersOnScreen[0] / 2) - (len(str) / 2), (lettersOnScreen[0] / 2) + (len(str) / 2) + 1):
        if xHeads[x] == -1:
            defTemp = False
    return defTemp

def getColor(fx,fy):
    defTemp=xHeads[fx]-fy

    if (maxCol>defTemp>0):
        return defTemp
    else:
        return maxCol-1


try:
    fo = open("indata.txt", "r+")
    str = fo.readline()
    # Close opend file
    fo.close()
except:
    str = ''
str = str.upper()  # for better placement


# Pygame init
pygame.init()
temp = pygame.display.Info()
displLength = (temp.current_w, temp.current_h)
surface = pygame.display.set_mode(displLength, pygame.FULLSCREEN)
# Font init
pygame.font.init()
fontObj = pygame.font.Font(pygame.font.get_default_font(), 14)
sampleLetter = fontObj.render('_', False, (0, 111, 0))
letterSize = (sampleLetter.get_width(), sampleLetter.get_height())
lettersOnScreen = (int(float(displLength[0]) / letterSize[0]),
                   int(float(displLength[1]) / letterSize[1]))

# color init
colorList = [(255, 255, 255)]
primeColors = len(colorList)+1
colorList += [(10, 210, 10)] * ((lettersOnScreen[1] - 10))
endColors = len(colorList)
colorList += [(0, 150, 0),(0, 100, 0),(0, 0, 0)]
endColors = len(colorList) - endColors+1

maxCol = len(colorList)


# char generator
letters = [[0 for _ in xrange(lettersOnScreen[1] + 1)] for _ in xrange(lettersOnScreen[0])]
char = chr(random.randint(32, 126))

for y in xrange(lettersOnScreen[1] + 1):
    for x in xrange(lettersOnScreen[0]):
        letters[x][y] = [fontObj.render(char, False, colorList[col]) for col in xrange(maxCol)]
        char = chr(random.randint(32, 126))


# word write
wordMode = False
if len(str) > 0:
    wordMode = True
    for x in xrange((lettersOnScreen[0] / 2) - (len(str) / 2),
                    (lettersOnScreen[0] / 2) + (len(str) / 2)):
        letters[x][lettersOnScreen[1] / 2] = [fontObj.render(str[x - ((lettersOnScreen[0] / 2) - (len(str) / 2))],
                                                             False, (255, 255, 255))
                                              for col in xrange(maxCol)]

    for y in xrange(lettersOnScreen[1] / 2 + 1,
                    lettersOnScreen[1] + 1):
        for x in xrange((lettersOnScreen[0] / 2) - (len(str) / 2),
                        (lettersOnScreen[0] / 2) + (len(str) / 2)):
            letters[x][y] = [fontObj.render(char, False, (0, 0, 0)) for col in xrange(maxCol)]
            char = chr(random.randint(32, 126))

    if len(str) % 2 == 1:

        letters[(lettersOnScreen[0] / 2) + (len(str) / 2)][lettersOnScreen[1] / 2] = \
            [fontObj.render(str[len(str) - 1], False, (255, 255, 255)) for col in xrange(maxCol)]

        for y in xrange(lettersOnScreen[1] / 2 + 1,
                        lettersOnScreen[1] + 1):
            letters[(lettersOnScreen[0] / 2) + (len(str) / 2)][y] = \
                [fontObj.render(char, False, (0, 0, 0)) for col in xrange(maxCol)]
            char = chr(random.randint(32, 126))

if wordMode:
    xHeads = [-1 for _ in xrange(lettersOnScreen[0] + 1)]
else:
    xHeads = [0 for _ in xrange(lettersOnScreen[0] + 1)]


# 1st loop - word write, no char switch
notDone = True
ticksLeft = lettersOnScreen[1] + maxCol
while ticksLeft > 0 and (notDone) and (wordMode):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notDone = False
        if event.type == pygame.KEYDOWN:
            notDone = False
    if IsWritten():
        ticksLeft -= 1
    if random.randint(1, 2) == 1:
        randomInt = random.randint(0, lettersOnScreen[0])
        if wordMode:
            if xHeads[randomInt] == -1:
                xHeads[randomInt] = 1
            if random.randint(1, 6):
                randomInt = random.randint((lettersOnScreen[0] / 2) - len(str),
                                           (lettersOnScreen[0] / 2) + len(str) + 1)
                if xHeads[randomInt] == -1:
                    xHeads[randomInt] = 1
        else:
            if xHeads[randomInt] == 0:
                xHeads[randomInt] = 1
    for x in xrange(lettersOnScreen[0]):
        col = 0
        counter = xHeads[x]
        while (counter > 0) and (col < maxCol):
            if (counter < lettersOnScreen[1] + 2) and (col < primeColors or
                                    col > (maxCol - endColors)):
                surface.blit(letters[x][counter - 1][col], (x * letterSize[0],
                                                            (counter - 1) * letterSize[1]))
            col += 1
            counter -= 1
        if xHeads[x] > 0:
            xHeads[x] += 1
        if xHeads[x] - maxCol > lettersOnScreen[1]:
            xHeads[x] = 0

    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(20)

# word delete
if len(str) % 2 == 1:
    strLen = (lettersOnScreen[0] / 2) + (len(str) / 2) + 1
else:
    strLen = (lettersOnScreen[0] / 2) + (len(str) / 2)

for x in xrange((lettersOnScreen[0] / 2) - (len(str) / 2),
                strLen):
    letters[x][lettersOnScreen[1] / 2] = \
        [fontObj.render(str[x - ((lettersOnScreen[0] / 2) - (len(str) / 2))], False, colorList[col])
         for col in xrange(maxCol)]

char = chr(random.randint(32, 126))
for y in xrange(lettersOnScreen[1] / 2 + 1,
                lettersOnScreen[1] + 1):
    for x in xrange((lettersOnScreen[0] / 2) - (len(str) / 2),
                    (lettersOnScreen[0] / 2) + (len(str) / 2) + 1):
        letters[x][y] = [fontObj.render(char, False, colorList[col]) for col in xrange(maxCol)]
        char = chr(random.randint(32, 126))


# main matrix, has char switch
while notDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            notDone = False
        if event.type == pygame.KEYDOWN:
            notDone = False
    if random.randint(1, 2) == 1:
        randomInt = random.randint(0, lettersOnScreen[0])
        if xHeads[randomInt] <= 0:
            xHeads[randomInt] = 1
    for x in xrange(lettersOnScreen[0]):
        col = 0
        counter = xHeads[x]
        # main loop for redraw
        while (counter > 0) and (col < maxCol):
            if (counter < lettersOnScreen[1] + 2) and (col < primeColors or
                                    col > (maxCol - endColors)):
                surface.blit(letters[x][counter - 1][col], (x * letterSize[0],
                                                            (counter - 1) * letterSize[1]))
            col += 1
            counter -= 1

        # charswirch
        randomInt = random.randint(1, maxCol - 1)
        charPosY = xHeads[x] - randomInt
        if (lettersOnScreen[1] - 1 > charPosY > 0):
            temp = letters[x][charPosY]
            randomX = random.randint(1, lettersOnScreen[0] - 1)
            randomY = random.randint(1,lettersOnScreen[1] - 1)

            surface.blit(letters[x][charPosY][maxCol - 1], (x * letterSize[0],
                                                            charPosY * letterSize[1]))
            surface.blit(letters[randomX][randomY][maxCol - 1], (randomX * letterSize[0],
                                                            randomY * letterSize[1]))
            # char swap
            letters[x][charPosY] = letters[randomX][randomY]
            letters[randomX][randomY] = temp

            surface.blit(letters[x][charPosY][randomInt], (x * letterSize[0], charPosY * letterSize[1]))
            surface.blit(letters[randomX][randomY][getColor(randomX,randomY)],
                         (randomX * letterSize[0], randomY * letterSize[1]))
        # check if is out of screen
        if xHeads[x] > 0:
            xHeads[x] += 1
        if xHeads[x] - maxCol > lettersOnScreen[1]:
            xHeads[x] = 0

    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(20)