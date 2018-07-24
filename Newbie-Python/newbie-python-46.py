n = int(input())
money = int(input())

x = []
for a in range(n):
    presents = input()
    x.append(presents)


every = 0
for item in x:
    if item == "sand clock":
        price = 2.20
    elif item == "magnet":
        price = 1.50
    elif item == "cup":
        price = 5.00
    elif item == "t-shirt":
        price = 10.00

    
    every += price

if money >= every:
    final = money - every
    final = "%.2f" % final
    print("Santa Claus has " + str(final) + " more leva left!")
elif every > money:
    final = every - money
    final = "%.2f" % final
    print("Santa Claus will need " + str(final) + " more leva.")




