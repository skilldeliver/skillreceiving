n = int(input())

string_list = [input() for i in range(n)]

for i in string_list:
    for j in range(len(i)):
        if j % 2 == 0:
            print(i[j], end="")
    print(end=" ")
    for j in range(len(i)):
        if j % 2 != 0:
            print(i[j], end="")
    print("")