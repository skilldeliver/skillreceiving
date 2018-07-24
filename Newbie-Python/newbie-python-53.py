n = int(input())
a = int(input())


c = 0

for i in range(n):
    i += 1
    hours = int(input())

    if i % 2 == 0 and hours % 2 == 0:
        per = 68 
    elif i % 2 != 0 and hours % 2 == 0:
        per = 49
    elif i % 2 == 0 and hours % 2 != 0:
        per = 65
    elif i % 2 != 0 and hours % 2 != 0:
        per = 30

    c += a * per

    
allEnergy = 100 * a * n
energyLeft = allEnergy - c
energyLeftDanc = energyLeft / a / n

if c <= (allEnergy / 2):
    energyLeftDanc = "%.2f" % energyLeftDanc
    print("They feel good! Energy left: " + str(energyLeftDanc))

elif c >= (allEnergy / 2):
    energyLeftDanc = "%.2f" % energyLeftDanc
    print("They are wasted! Energy left: " + str(energyLeftDanc))









