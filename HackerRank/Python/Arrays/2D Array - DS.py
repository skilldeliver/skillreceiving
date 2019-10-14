# Complete the hourglassSum function below.
# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def hourglassSum(arr):
    top = -1000000000
    for i in range(4):
        for j in range(4):
            tot = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i + 2][j:j+3])
            if tot > top:
                top = tot
    return top  