
sum = float(input())
mesec = int(input())

simple = sum
complex = sum

for i in range(mesec):

    simple  += (sum * 0.03)
    complex += complex * 0.027


print("Simple interest rate: ", end = "")
print(str("%.2f" % simple) + " lv.")
print("Complex interest rate: ", end = "")
print(str("%.2f" % complex) + " lv.")


if simple >= complex:
    win = simple - complex
    win = "%.2f" % win
    print("Choose a simple interest rate. You will win " + str(win) + " lv.")

else:
    win = complex - simple
    win = "%.2f" % win
    print("Choose a complex interest rate. You will win " + str(win) + " lv.")




