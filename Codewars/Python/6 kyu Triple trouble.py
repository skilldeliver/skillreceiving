def triple_double(num1, num2):
    trip = ""
    num1 = list(str(num1))    
    leng = 1
    
    for i in range(1, len(num1)):
        if num1[i] == num1[i-1]:
            leng += 1
        else: leng = 1
        if leng == 3: trip = num1[i]
    if list(str(num2)).count(trip) == 2: return 1
    return 0