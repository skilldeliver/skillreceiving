while True:
    print("This is a kilometer-meter convertror")
    print ("\n")
    print ("Type 'km-m' if u want to convert from kilometers to meters")
    print ("Type 'm-km' if u want to convert from meters to kilometers")
    print ("Type 'close' to close the programm")

    user_input = input(": ")

    if user_input == "close":
        break

      elif user_input == "km-m":
         num1 = float(input("Enter kilometers: "))

         result = str(num1 / 1000)
         print(num1 + " kilometers is" + result + " meters"

      else:
        print("Unknow input")


 