
import math
n = int(input())
m = float(input())
c = m
km = 0
for a in range(n):
    per = int(input())
    perc = per / 100
    m += m * perc
    km += m
        
all = km + c



if all >= 1000:
    all = all - 1000
    all = math.ceil(all)
    print("You've done a great job running " + str(all) + " more kilometers!" )
else:
    all = 1000 - all
    all = math.ceil(all)
    print("Sorry Mrs. Ivanova, you need to run " + str(all) + " more kilometers")

