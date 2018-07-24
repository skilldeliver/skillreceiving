h = int(input())
x = int(input())
y = int(input())

ab1 = False
ab2 = False
border = False
ab1R = False
ab2R = False

if (x > h and x < h * 2) and (y > h and y < h * 4): ab1 = True
if (x > 0 and x < h * 3) and (y > 0 and y < h): ab2 = True
if (y == h and (x > h and x < 2 * h)): border = True

if (x < h or x > h * 2) or (y < h or y > h * 4): ab1R = True
if (x < 0 or x > h * 3) or (y < 0 or y > h): ab2R = True


if ab1 or ab2 or border: print("inside")
elif ab1R and ab2R: print("outside")
else: print("border")
