budget = float(input())
season = str(input())


if budget <= 100:
    print("Somewhere in Bulgaria")
    if season == "summer":
        price = budget * (30 / 100)
        price = float(price)
        
        print("Camp - ", "%.2f" % price)
    elif season == "winter":
        price = budget * (70 / 100)
        price = float(price)
        
        print("Hotel - ", "%.2f" % price)


if budget <= 1000 and budget > 100:
    print("Somewhere in Balkans")
    if season == "summer":
        price = budget * (40 / 100)
        price = float(price)
       
        print("Camp - ", "%.2f" % price)
    elif season == "winter":
        price = budget * (80 / 100)
        price = float(price)
        
        print("Hotel - ", "%.2f" % price)

if budget > 1000:
    print("Somewhere in Europe")
    if season == "summer":
        price = budget * (90 / 100)
        price = float(price)
        
        print("Camp - ", "%.2f" % price)
    elif season == "winter":
        price = budget * (90 / 100)
        price = float(price)
        
        print("Hotel - ", "%.2f" % price)



