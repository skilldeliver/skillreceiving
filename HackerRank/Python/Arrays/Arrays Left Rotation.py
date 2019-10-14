# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Complete the rotLeft function below.

def rotLeft(a, d):
    for i in range(d):
        a.append(a.pop(0))
    return a
