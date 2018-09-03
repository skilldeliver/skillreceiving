def find_missing_letter(chars):
    alp = "abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".upper()
    return list(set(list(alp[alp.index(chars[0]):alp.index(chars[len(chars) - 1]) + 1])) - set(chars))[0]