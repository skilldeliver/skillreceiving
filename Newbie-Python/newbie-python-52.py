budget = float(input())
season = input()


if budget <= 100:
    type = "Economy class"
    if season == "Summer":

        car = "Cabrio"
        price = budget * 0.35

    elif season == "Winter":

        car = "Jeep"
        price = budget * 0.65


elif budget > 100 and budget <= 500:
    type = "Compact class"
    if season == "Summer":

        car = "Cabrio"
        price = budget * 0.45

    elif season == "Winter":

        car = "Jeep"
        price = budget * 0.80

elif budget > 500:
    type = "Luxury class"
    car = "Jeep"
    price = budget * 0.90


print(type)
print(car + " - " + str("%.2f" % price))

