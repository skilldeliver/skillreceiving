def middle_permutation(s):
    s = ''.join(sorted(s))
    return s[int(len(s) / 2)] + middle_permutation(s.replace(s[int(len(s) / 2)],'')) if len(s) % 2 else s[int(len(s) / 2 - 1)] + s.replace(s[int(len(s) / 2 - 1)],'')[::-1]