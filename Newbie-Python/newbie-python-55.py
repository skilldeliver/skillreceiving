import math

sec = float(input())
meters = float(input())
SecInMet= float(input())


neededM = meters * SecInMet
MoreSec = math.floor(meters / 15) * 12.5


allTime = neededM + MoreSec


if sec > allTime:

    result = allTime
    
    result = "%.2f" % result

    print("Yes, he succeeded! The new world record is %s seconds." % result)


elif sec <= allTime:
    result = allTime - sec
    
    result = "%.2f" % result

    print("No, he failed! He was %s seconds slower." % result)

