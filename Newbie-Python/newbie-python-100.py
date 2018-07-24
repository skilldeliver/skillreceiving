import math

participants = int(input())
forFirstPlace = int(input())

secondPlace = forFirstPlace - (forFirstPlace * 0.20)
thirdPlace = secondPlace - (secondPlace * 0.10)

allPlace = forFirstPlace + secondPlace + thirdPlace

half = int(participants / 2)

if allPlace >= half:
    more = allPlace - half
    more = int(more)
    print("First three languages have %s votes more" % more)
else:
    more = half - (allPlace + 1)
    more = int(more)
    print("First three languages have %s votes less of half votes" % more)





