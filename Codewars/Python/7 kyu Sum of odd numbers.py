def row_sum_odd_numbers(n):
    o = -1
    odds = []
    for _ in range(n * (n + 1) // 2):
        o += 2
        odds.append(o)
    
    return sum(odds[len(odds) - n: len(odds)])