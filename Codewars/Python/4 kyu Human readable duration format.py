from __future__ import print_function

def format_duration(sec):

    if sec == 0:
        return "now"

    hold = "year", "day", "hour", "minute", "second"
    intervals = [31536000, 86400, 3600, 60, 1]
    formated = []
    for count in intervals:
        value = sec // count
        formated.append(value)
        sec -= value * count

    arr = []
    index = -1

    for el in formated:
        index += 1
        if el != 0:
            if el == 1:
                arr.append((el, hold[index]))
            else:
                arr.append( (el, hold[index] + "s"))
                
    index = -1

    string = ""
    for el in arr:
        index += 1
        if index < len(arr) - 2:
            string += "".join((str(el[0]), " ", str(el[1]), ", "))

    if len(arr) == 1:
        string += str(arr[len(arr) - 1][0]) + " " + str(arr[len(arr) - 1][1])
    else:
        string += str(arr[len(arr) - 2][0]) + " " + str(arr[len(arr) - 2][1]) + " " + "and" + " " + str(arr[len(arr) - 1][0]) + " " + str(arr[len(arr) - 1][1])
    return string