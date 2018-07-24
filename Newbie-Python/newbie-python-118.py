import sys
import time
#n = ""
#c = 0
#stop = False
#for i in range(100):
#    if stop: break
#    n = input()
#    c += 1
#    for j in n:
#        if j in "0 1 2 3 4 5 6 7 8 9": pass
#        else:
#            stop = True
#            break
#print(c - 1)


#n = int(input())

#for i in range(n + 1):
#    i += 1
#    for n in range(i):
#        print(i, end = " ")
#    print()

damagePesho = int(input())
damegeGosho = int(input())
healthPesho = 100
healthGosho = 100

k = 0
while 1:
    k += 1
    if healthGosho <= 0 or healthPesho <= 0:
        break
    if k % 2 == 0:
        healthPesho -= damegeGosho
        if healthGosho <= 0 or healthPesho <= 0:
            break
        text = "Gosho used Thunderous fist and reduced Pesho to " + str(healthPesho) + " health."
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1) 
        print()
    else:
        healthGosho -= damagePesho
        if healthGosho <= 0 or healthPesho <= 0:
            break
        text = "Pesho used Roundhouse kick and reduced Gosho to "+ str(healthGosho) + " health."
        for i in text:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.1)
        print()
    if k % 3 == 0:
        healthGosho += 10
        healthPesho += 10
        
if healthPesho <= 0:
    text = "Gosho won in " + str(k) + "th round."
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)
else:
    text = "Pesho won in " + str(k) + "th round."
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.1)

#condition = True
#a = int(input())
#b = int(input())
#n1 = a
#n2 = n1 + 1
#n3 = n2 + 1
#n4 = n3 + 1
#n5 = n3 + 1


##if a <= n1 and n1 < n2 and n2 < n3 and n3 < n4 and n4 < n5 <= b:

#for i in range(100)

#firstN = int(input())
#secN = int(input())
#MagN = int(input())

#sum = 0

#for i in range(firstN, secN):
#    for k in range(firstN, secN):
#        sum = i + k
#        if sum == MagN:
#            text = str(i) + " " + str(k) + "=" + str(MagN)




#print(text)

#letters = ["a", "b", "c", "d", "e", "f", "g", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

#firstLetter = input()
#secondLetter = input()
#thirdLetter = input()

#temp = -1
#n1 = 0
#n2 = 0
#n3 = 0

#for i in letters:
#    temp += 1
#    if i == firstLetter:
#        n1 = temp
#    if i == secondLetter:
#        n2 = temp
#    if i == thirdLetter:
#        n3 = temp

#for i in range(n1, n2 + 1):
#    for j in range(n1, n2 + 1):
#        for k in range(n1, n2 + 1):
#            result = letters[i] + " " + letters[j] + " " + letters[k]
#            if not thirdLetter in result:
#                print(letters[i] + letters[j] + letters[k], end = " ")




