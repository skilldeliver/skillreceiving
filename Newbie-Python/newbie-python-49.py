n1 = int(input())
n2 = int(input())

x = []
y = []
for a in range(n1, n2):
    a += 1
    x.append(a)
    for item in x:
        for ele in str(item):
            if int(ele) % 2 != 0:
                y.append(item)



print(y)



