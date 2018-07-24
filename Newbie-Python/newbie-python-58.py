cap = int(input())
fans = int(input())

a = 0
b = 0
c = 0
d = 0


for i in range(fans):
    sector = input()

    if sector == "A":
        a += 1

    elif sector == "B":
        b += 1

    elif sector == "V":
        c += 1

    elif sector == "G":
        d += 1


n1 = (a / fans) * 100
n2 = (b / fans) * 100
n3 = (c / fans) * 100
n4 = (d / fans) * 100

stadion = (fans / cap ) * 100

n1 = "%.2f" % n1
n2 = "%.2f" % n2
n3 = "%.2f" % n3
n4 = "%.2f" % n4
stadion = "%.2f" % stadion

print(str(n1) + "%")
print(str(n2) + "%")
print(str(n3) + "%")
print(str(n4) + "%")
print(str(stadion) + "%")

    
























