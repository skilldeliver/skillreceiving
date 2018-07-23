def solve(s, d, m):
    total = 0
    segment_sum = 0
    for i in range(0, (len(s) - m) + 1):
        for j in range(i, i + m):
            segment_sum += s[j]
        if segment_sum == d:
            total += 1
        segment_sum = 0
            
    return total
            

if __name__ == '__main__':
    n = int(input())

    s = list(map(int, input().rstrip().split()))

    dm = input().split()

    d = int(dm[0])

    m = int(dm[1])

    result = solve(s, d, m)
    print(result)