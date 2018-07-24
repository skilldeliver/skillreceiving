type = input()
rows  = int(input())
cols = int(input())
price = 0

if type == "Premiere": price = 12.00
elif type == "Normal": price = 7.50
elif type == "Discount": price = 5.00

print("%.2f" % ((rows * cols) * price), "leva")