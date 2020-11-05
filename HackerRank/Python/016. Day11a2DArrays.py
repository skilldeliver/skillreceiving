arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

cur_sum, max_sum = 0, -100000

for j in range(4):
    for i in range(4):
        for list1 in range(i, i + 3):
            cur_sum += arr[j][list1]
        cur_sum += arr[j + 1][i + 1]
        for list2 in range(i, i + 3):
            cur_sum += arr[j + 2][list2]
        if cur_sum > max_sum:
            max_sum = cur_sum
        cur_sum = 0

print(max_sum)

        

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0