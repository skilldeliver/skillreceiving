nights = int(input())
dest = input()
trans = input()

if nights >= 1 and nights <= 10:
    if dest == "Miami":
        par = 24.99
        child = 14.99

    elif dest == "Canary Islands":
        par = 32.50
        child = 28.50

    elif dest == "Philippines":
        par = 42.99
        child = 39.99

elif nights > 11 and nights <= 15:
    if dest == "Miami":
        par = 24.99
        child = 14.99

    elif dest == "Canary Islands":
        par = 32.50
        child = 28.50

    elif dest == "Philippines":
        par = 42.99
        child = 39.99


elif nights > 15:

    if dest == "Miami":
       par = 24.99
       child = 14.99

    elif dest == "Canary Islands":
        par = 32.50
        child = 28.50

    elif dest == "Philippines":
        par = 42.99
        child = 39.99


if trans == "train":
    tpar = 22.30
    tchild = 12.50

elif trans == "bus":
    tpar = 45.00
    tchild = 37.00
elif trans == "airplane":
    tpar = 90.00
    tchild = 68.50


destination = (nights * ((2 * par) + (3 * child)))

transport = ((2 * tpar) + (3 * tchild))

totatDest = destination * 1.25

all = totatDest + transport

print("%.3f" % all)

