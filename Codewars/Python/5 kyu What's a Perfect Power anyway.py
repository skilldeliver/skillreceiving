def isPP(n):
    from math import log, sqrt
    if n < 4: return None
    
    sr = round(sqrt(n),6)
    if sr == round(sr): return [sr, 2]
    
    for m in range(2,n//2):
        k = round(log(n, m),6)
        if k == round(k): return [m, k]
    return None