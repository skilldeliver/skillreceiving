


while True:
    test = input("Do you want to test? ")

    if test == "Yes" or test == "y":

        n = int(input())
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0




        for i in range(n):
            points = float(input())

            if points >= 0 and points <= 22.5:
                a += 1 
            elif points > 22.50 and points <= 40.5:
                b += 1
            elif points > 40.5 and points <= 58.5:
                c += 1
            elif points > 58.5 and points <= 76.5:
                d += 1
            elif points > 76.5 and points <= 100:
                e += 1



        oneMark = 100 / n

        per1 = oneMark * a
        per2 = oneMark * b
        per3 = oneMark * c
        per4 = oneMark * d
        per5 = oneMark * e

        per1 = "%.2f" % per1
        per2 = "%.2f" % per2
        per3 = "%.2f" % per3
        per4 = "%.2f" % per4
        per5 = "%.2f" % per5

        print(str(per1) + "% poor marks")
        print(str(per2) + "% satisfactory  marks")
        print(str(per3) + "% good marks")
        print(str(per4) + "% very good marks")
        print(str(per5) + "% excellent marks")

    elif test == "No" or test == "n":
        break
    else:
        print("Yes or No?")