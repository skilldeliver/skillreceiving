import random
import math
import pygame
import time

a = dir(random)
b = dir(math)
c = dir(pygame)
d = dir(time)

line = 0
line1 = 0
line2 = 0
line3 = 0
line4 = 0
randomMod = 61
mathMod = 54
pygameMod = 334
timeMod = 25

for item in a:

    line += 1
    lin = str(line)
    print(lin + "." + item)

for item in b:

    line1 += 1
    lin1 = str(line1)
    print(lin1 + "." + item)

for item in c:

    line2 += 1
    lin2 = str(line2)
    print(lin2 + "." + item)

for item in d:

    line3 += 1
    lin3 = str(line3)
    print(lin3 + "." + item)
