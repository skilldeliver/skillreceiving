n1 = int(input())
n2 = int(input())
op = str(input())




if op == "+":
    sum = n1 + n2
    if sum % 2 == 0:
        print(n1, op, n2, "=", sum, " - even")
    else:
        print(n1, op, n2, "=", sum, " - odd")

elif op == "-":
    sum = n1 - n2
    if sum % 2 == 0:
        print(n1, op, n2, "=", sum, " - even")
    else:
        print(n1, op, n2, "=", sum, " - odd")

elif op == "*":
    sum = n1 * n2
    if sum % 2 == 0:
        print(n1, op, n2, "=", sum, " - even")
    else:
        print(n1, op, n2, "=", sum, " -odd")

elif op == "/":
    if n1 == 0 or n2 == 0:
        print("Cannot devide by zero")
    else:
        sum = n1 / n2
        print(n1, op, n2, "=", sum)

elif op == "%":
    if n1 == 0 or n2 == 0:
        print("Cannot devide by zero")
    else:
        sum = n1 % n2
        print(n1, op, n2, "=", sum)






