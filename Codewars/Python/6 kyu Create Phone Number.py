def create_phone_number(n):
    n = [str(i) for i in n]
    return f"({''.join(n[0:3])}) {''.join(n[3:6])}-{''.join(n[6:10])}"