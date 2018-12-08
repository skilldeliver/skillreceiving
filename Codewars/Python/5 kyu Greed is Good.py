def score(dice):
    total = int()
    points = (1000, 200, 300, 400, 500, 600)
    alist = [int() for _ in range(6)]
    
    for d in dice:
        alist[d - 1] += 1
        
    for i in range(0, len(alist)):
        if alist[i] >= 3:
            total += points[i]
            alist[i] -= 3
        if i == 0:
            total += alist[i] * 100 
        elif i == 4:
            total += alist[i] * 50
    return total
