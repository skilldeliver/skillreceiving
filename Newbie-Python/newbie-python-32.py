budget = float(input())
cat = str(input())
count = int(input())


if cat == "VIP":
    ticket = 499.99
    if count >= 1 and count <= 4:
        transport = budget * (75 / 100)
    elif count >= 5 and count <= 9:
        transport = budget * (60 / 100)
    elif count >= 10 and count <= 24:
        transport = budget * ( 50 / 100)
    elif count >= 25 and count <= 49:
        transport = budget * ( 40 / 100)
    elif count >= 50:
        transport = budget * (25 / 100)

    last = transport + ( ticket * count )
    if last < budget:
        left = budget - last
        print("Yes! You have", "%.2F" % left, "leva left")
    else:
        notEnough = last - budget
        print("Not enough money! You need ", "%.2F" % notEnough, " leva.")
  


elif cat == "Normal":
    ticket = 249.99
    if count >= 1 and count <= 4:
        transport = budget * (75 / 100)
    elif count >= 5 and count <= 9:
        transport = budget * (60 / 100)
    elif count >= 10 and count <= 24:
        transport = budget * ( 50 / 100)
    elif count >= 25 and count <= 49:
        transport = budget * ( 40 / 100)
    elif count >= 50:
        transport = budget * (25 / 100)

    last = transport + ( ticket * count )
    if last < budget:
        left = budget - last
        print("Yes! You have", "%.2F" % left, "leva left")
    else:
        notEnough = last - budget
        print("Not enough money! You need ", "%.2F" % notEnough, " leva.")


