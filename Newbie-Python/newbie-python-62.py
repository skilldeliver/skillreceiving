n = int(input())
x = (4 * n) + 1
y = (2 * n) + 1
pointsIndex = 0
for i in range(y):
    i += 1
    if i == 2:
        pointsIndex = 1
    else:
        pointsIndex += 1

    if i == 1:
        tagsIndex = x
        pointsIndex = 0
        points = pointsIndex * "."
        tags = "#" * tagsIndex
        print(tags)
    elif i > 1:
        tagsIndex -= 2
        pointsIndex = 0
        points = pointsIndex * "."
        print(points + tags + points)


