n = int(input())

def bin_consecutive(n):
    if n == 1: return 1
    bin_num, num, binaries = "", 1, []
     
    while num <= n: #get all binary numbers up to the input n
        binaries.append(num)
        num *= 2

    for i in range(len(binaries) - 1, -1, -1): # get the binary num of the input n
        if n - binaries[i] >= 0:
            n -= binaries[i]
            bin_num += "1"
        elif bin_num and bin_num[0] == "1": bin_num += "0"

    max_count, count = 0, 0
    for i in range(0, len(bin_num)): # count all 1s in the binary num
        if bin_num[i] == "1":
            count += 1
        elif bin_num[i] == "0":
            if count > max_count:
                max_count = count
            count = 0
    if max_count == 0: max_count = count
    if count > max_count:max_count = count
    
    return max_count


print(bin_consecutive(n))
