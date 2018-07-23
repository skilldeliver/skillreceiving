# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    total = 0
    for i in arr:
        total += i
        
    tempArr = total - arr[0]
    minArr = tempArr
    maxArr = tempArr
    for i in arr:
        tempArr = total - i
        if tempArr < minArr:
            minArr = tempArr
        if tempArr > maxArr:
            maxArr = tempArr
        
    print(minArr, maxArr)
 

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)