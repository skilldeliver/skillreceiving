
if lenght <= 100:
            return lenght
        elif lenght > 100:
            lenght = input("Huh, that a big password. Try with smaller one: ")
        else:
            lenght = input("Enter a integer, please. Try again: ")




            if lenght >= 100:
        return lenght

    if DoCaps == "yes" or DoCaps == "y":
        CapLetters ='ABCDEFGIJKLMNOPQRSTUVWXYZ'
        return CapLetters
    elif DoCaps == "no" or DoCaps == "n":
        f = 5 + 5

        if DoSigns == "yes" or  DoSigns == "y":
        signs = '`~!@#$%^&*()_+-=[]{};:\'"<>,.?/|\\'
        return signs
    elif DoSigns == "no" or DoSigns == "n":
