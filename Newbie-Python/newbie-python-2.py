while True:
    print("Опции: ")
    print("\n")
    print("Въведете 'събиране' за да съберете две числа")
    print("Въведете 'изваждане' за да изваждане две числа")
    print("Въведете 'умножаване' за да умножите две числа")
    print("Въведете 'разделяне' за да разделите две числа")
    print("Въведете 'затваряне' за да затворите програмата")
    print("\n")
    user_input = input("Моля въведете опция: ")

    if user_input == "затваряне":
        break
    elif user_input == "събиране":
        num1 = float(input("Въведете първото число: "))
        num2 = float(input("Въведете второто число: "))

        result = str(num1 + num2)
        print("Отговорът е: " + result)
        print("\n")
    elif user_input == "изваждане":
        num3 = float(input("Въведете първото число: "))
        num4 = float(input("Въведете второто число: "))

        result = str(num3 - num4)
        print("Отговорът е: " + result)
        print("\n")
    elif user_input == "умножаване":
        num5 = float(input("Въведете първото число: "))
        num6 = float(input("Въведете второто число: "))

        result = str(num5 * num6)
        print("Отговорът е: " + result)
        print("\n")
    elif user_input == "разделяне":
        num7 = float(input("Въведете първото число: "))
        num8 = float(input("Въведете второто число: "))

        result = str(num7 / num8)
        print("Отговорът е: " + result)
        print("\n")

    else:
        print("Неналична опция, опитайте пак...")
        print("\n")




