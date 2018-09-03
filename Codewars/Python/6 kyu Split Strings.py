def solution(s):
    n = [s[i:i+2] for i in range(0, len(s), 2)]   
    if len(s) % 2 != 0: n[len(n) - 1] += "_"
    
    return n