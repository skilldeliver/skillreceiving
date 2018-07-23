def timeConversion(s):
    hours   = s[0:2]
    minutes = s[3:5]
    seconds = s[6:8]
    zone = s[8: len(s)]
    
    if zone == "PM" and hours != "12":
        temp = 0
        if hours[0] == "0":
            temp = int(hours[1]) + 12
        else:
            temp = int(hours) + 12
        if temp < 10: hours = "0" + str(temp)
        else: hours = str(temp)
        
    if zone == "AM" and hours == "12":
        hours = "00"
    
    return hours + ":" + minutes + ":" + seconds

s = " "
while s != "break":
    s = input()
    result = timeConversion(s)
    print(result + '\n')