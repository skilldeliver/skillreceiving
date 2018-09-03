def openOrSenior(data):
    # Hmmm.. Where to start?
    arr = []
    for i in data:
        if i[0] >= 55 and i[1] > 7: arr.append("Senior")
        else: arr.append("Open")
    return arr