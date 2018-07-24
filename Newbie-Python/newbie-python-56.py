moves = int(input())

result = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

for i in range(moves):
    turn = int(input())
    
    if turn >= 0 and turn <= 9:
        result += turn * (20 / 100)
        a += 1
    elif turn >= 10 and turn <= 19:
        result += turn * (30 / 100)
        b += 1
    elif turn >= 20 and turn <= 29:
        result += turn * (40 / 100)
        c += 1
    elif turn >= 30 and turn <= 39:
        result += 50
        d += 1       
    elif turn >= 40 and turn <= 50:
        result += 100
        e += 1
    else:
        f += 1
        result -= result / 2
    
oneNum = 100 / moves
n1 = oneNum * a
n2 = oneNum * b
n3 = oneNum * c 
n4 = oneNum * d
n5 = oneNum * e
n6 = oneNum * f

n1 = "%.2f" % n1
n2 = "%.2f" % n2
n3 = "%.2f" % n3
n4 = "%.2f" % n4
n6 = "%.2f" % n6
n5 = "%.2f" % n5

print("%.2f" % result)
print("From 0 to 9: " + str(n1) + "%")
print("From 10 to 19: " + str(n2) + "%")
print("From 20 to 29: " + str(n3) + "%")
print("From 30 to 39: " + str(n4) + "%")
print("From 40 to 50: " + str(n5) + "%")
print("Invalid numbers: " + str(n6) + "%")







    
