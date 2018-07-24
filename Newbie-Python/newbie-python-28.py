hourExam = int(input())
minuteExam = int(input())
hourCome = int(input())
minuteCome = int(input())

hourInMinExam = hourExam * 60
hourInMinCome = hourCome * 60

totalHourMinExam = hourInMinExam + minuteExam
totalHourMinCome = hourInMinCome + minuteCome

earlyMin = totalHourMinExam - totalHourMinCome

if (totalHourMinExam == totalHourMinCome):
    print("On time")

if (totalHourMinCome < totalHourMinExam and totalHourMinExam - totalHourMinCome <= 30):
    print("On time")
    print(earlyMin, " minutes before the start")


if (totalHourMinCome < totalHourMinExam and totalHourMinExam - totalHourMinCome > 30 ):
    print("Early")
    if (totalHourMinExam - totalHourMinCome > 30 and totalHourMinExam - totalHourMinCome < 60):
        lateMinutes1 = totalHourMinExam - totalHourMinCome
        print(lateMinutes1, " minutes before the start")
    else:
        earlyHours = hourExam - hourCome
        earlyMinutes = minuteExam - minuteCome
        print(earlyHours, ":", "%.2f" % earlyMinutes, " hours before the start")

if (totalHourMinCome > totalHourMinExam):
    print("Late")
    if (totalHourMinCome - totalHourMinExam < 60):
        lateMinutes = totalHourMinCome - totalHourMinExam
        print(lateMinutes, " minutes after the start")
    else:
         lateHours = hourCome - hourExam
         lateMinutes = minuteCome - minuteExam       
         print(lateHours, ":","%.2f" % lateMinutes, " hours after the start")


    
    










