days = int(input())
type = str(input())
rate = str(input())




nights = (days - 1)


if type == "room for one person":
    one = 18.00
    sum = nights * one

    if rate == "positive":
        per = 0.25
        sum = sum + (sum * per)
        sum = round(sum, 2)
        print("%.2f" % sum)
    elif rate == "negative":
        per = 0.1
        sum = sum - (sum * per)
        sum = round(sum, 2)
        print("%.2f" % sum)
    

elif type == "apartment":
    one = 25.00
    sum = nights * one

    if days < 10:
        low = 0.3
    elif days >= 10 and days <= 15:
        low = 0.35
    elif days > 15:
        low = 0.5

    sum = sum - (sum * low)
    if rate == "positive":
        per = 0.25
        sum = sum + (sum * per)
        
        print("%.2f" % sum)
    elif rate == "negative":
        per = 0.1
        sum = sum - (sum * per)
        sum = round(sum, 2)
        print("%.2f" % sum)
    

elif type == "president apartment":
    one = 35.00
    sum = nights * one
    
    if days < 10:
        low = 0.1
    elif days >= 10 and days <= 15:
        low = 0.15
    elif days > 15:
        low = 0.2
    
    
    sum = sum - (sum * low)
    
    if rate == "positive":
       
       sum = sum + (sum * 0.25)
       sum = round(sum, 2)
       print("%.2f" % sum)

    elif rate == "negative":
        
        sum = sum - (sum * 0.1)
        sum = round(sum, 2)
        print("%.2f" % sum)
    


