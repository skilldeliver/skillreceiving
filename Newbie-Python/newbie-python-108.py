theList = open("realhuman_phill.txt", "r")
count = 0
for x in theList:
    count += 1
    print("Try: ", count)
    if x == "hello":
        print("Find")
        break
