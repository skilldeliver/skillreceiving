def permutations(string):
    from itertools import permutations   
    return list(set([''.join(p) for p in permutations(string)]))