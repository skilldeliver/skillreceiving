n = int(input())

for i in range(n):
    i += 1
    if i == 1:
        print(n * "*")
    elif i == n:
        print(n * "*")
    else:
        print("*", end = "")
        print(" " * (n - 2), end = "")
        print("*")

