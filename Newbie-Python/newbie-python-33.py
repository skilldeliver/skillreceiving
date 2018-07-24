month = str(input())
nights = int(input())



if month == "May" or month == "Octomber":
    studio = 50
    apartment = 65
    totalStd = nights * studio
    totalAp = nights * apartment

    if nights > 7 and nights <= 14:
        totalStd = totalStd * ( 5 / 100)
    elif nights > 14:
        totalStd = totalStd - (totalStd * 0.3)
        totalAp = totalAp - (totalAp * 0.1)

    totalStd = format(totalStd, ".2f")
    totalAp = format(totalAp, ".2f")
    print("Apartment:", totalAp, "lv.")
    print("Studio:", totalStd, "lv.")


elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    totalStd = nights * studio
    totalAp = nights * apartment
        
    if nights > 14:
        totalStd = totalStd - (totalStd * 0.2)
        totalAp = totalAp -(totalAp * 0.1)

    totalStd = format(totalStd, ".2f")
    totalAp = format(totalAp, ".2f")
    print("Apartment:", totalAp, "lv.")
    print("Studio:", totalStd, "lv.")

    

elif month == "Jule" or month == "August":
    studio = 76
    apartment = 77
    totalStd = nights * studio
    totalAp = nights * apartment

    if nights > 14:
        totalAp = totalAp - (totalAp * 0.1)

    totalStd = format(totalStd, ".2f")
    totalAp = format(totalAp, ".2f")
    print("Apartment:", totalAp, "lv.")
    print("Studio:", totalStd, "lv.")
