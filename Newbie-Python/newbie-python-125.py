points = int(input())
arena = input()
day = input()
condition = input()

per = 1

if day == "Monday" or day == "Wednesday": 
    per = 0.05
elif day == "Tuesday" or day == "Thursday": 
    per = 0.1
elif day == "Friday " or day == "Saturday": 
    per = 0.07

if condition == "Poor": price = 7000
elif condition == "Normal": price = 14000
elif condition == "Legendary": price = 21000



price2 = price - (price * per)
one = price2 / 5
print(per)
for i in range(1, 6):

    price -= one
    if price < one:
        break

print(price)
print(i)




