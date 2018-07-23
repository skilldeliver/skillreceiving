def birthdayCakeCandles(arr):
    largest = arr[0]
    for i in arr:
        if i > largest: largest = i
    result = 0
    for j in arr:
        if j == largest: result += 1
            
    return result


ar = list(map(int, input().rstrip().split()))

result = birthdayCakeCandles(ar)
print(str(result) + '\n')