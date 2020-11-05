def kangaroo(x1, v1, x2, v2): 
    for i in range(1000):
        x1 += v1
        x2 += v2
        if x1 == x2: return "YES"
    return "NO"

x1, v1, x2, v2 = map(int, input().split())

result = kangaroo(x1, v1, x2, v2)
print(result)