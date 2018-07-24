n = int(input())
n1 = int(n / 10)
n2 = int(n % 10)
list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "", "fifteen", "one hundred", "invalid number"]
list2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

if n < 0 or n > 100: print(list[17]) 
elif n == 100: print(list[16])
elif n >= 0 and n < 14 or n == 15: print(list[n])
elif n > 13 and n < 20: print(list[n2] + "teen")
elif n > 19 and n < 100 and n2 == 0: print(list2[n1 - 2]) 
else: print(list2[n1 - 2], list[n2])       