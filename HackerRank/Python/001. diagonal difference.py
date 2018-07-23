def diagonalDifference(arr):
    rightD = 0
    leftD = 0
    for i in range(len(arr)):
        rightD += arr[i][i]
        leftD += arr[i][len(arr) - 1 - i]
        
    total = rightD - leftD
    if total < 0: total *= -1
    return total

n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

print(arr)
result = diagonalDifference(arr)
print(str(result) + '\n')