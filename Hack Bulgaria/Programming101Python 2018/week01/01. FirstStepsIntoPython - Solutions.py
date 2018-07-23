

def sum_of_digits(n):
    return sum(int(i) for i in str(abs(n)))

def to_digits(n):
    return [int(i) for i in str(n)]

def fact_digits(n):
    fact = 1
    total = 0

    for i in str(n):
        for j in range(2, int(i) + 1):
            fact *= j
        total += fact
        fact = 1
    return total

def fibonacci(n):
    arr = []

    for i in range(0, n):
        if i == 0 or i == 1: arr.append(1 + 0)
        else: arr.append(arr[len(arr) - 1] + arr[len(arr) - 2])
    return arr

def fib_num(n):
    arr = []
    string = ""

    for i in range(0, n):
        if i == 0 or i == 1: arr.append(1 + 0)
        else: arr.append(arr[len(arr) - 1] + arr[len(arr) - 2])

    for el in arr:
        string += str(el)
    return string

def palindrome(arg):
    arg = str(arg)
    rev = ""

    for i in range(len(arg) - 1, -1, -1):
        rev += arg[i]

    return arg == rev

def count_vowels(arg):
    return sum(1 for i in arg if i.lower() in "aeoiuy")

def count_consonants(arg):
    return sum(1 for i in arg if i.lower() in "bcdfghjklmnpqrstvwxz")

def char_histogram(string):
    out_dict = {}
    for let in string:
        try:
            out_dict[let] += 1
        except KeyError:
            out_dict[let] = 1
        
    return out_dict 

if __name__ == "__main__":

    print("Sum of all digits of a number")
    print("---------------------------------")
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(123))
    print(sum_of_digits(6))
    print(sum_of_digits(-10))
    print("---------------------------------")
    print("  ")
    print("Turn a number into a list of digits")
    print("---------------------------------")
    print(to_digits(123))
    print(to_digits(99999))
    print(to_digits(123023))
    print("---------------------------------")
    print("  ")
    print("Factorial digits")
    print("---------------------------------")
    print(fact_digits(111))
    print(fact_digits(145))
    print(fact_digits(999))
    print("---------------------------------")
    print("  ")
    print("First nth members of Fibonacci")
    print("---------------------------------")
    print(fibonacci(1))
    print(fibonacci(2))    
    print(fibonacci(3))
    print(fibonacci(10))
    print("---------------------------------")
    print("  ")
    print("Fibonacci number")
    print("---------------------------------")
    print(fib_num(3))
    print(fib_num(10))
    print("---------------------------------")
    print("  ")
    print("Palindrome")
    print("---------------------------------")
    print(palindrome(121))
    print(palindrome("kapak"))
    print(palindrome("baba"))
    print("---------------------------------")
    print("  ")
    print("Vowels in a string")
    print("---------------------------------")
    print(count_vowels("Python"))
    print(count_vowels("Theistareykjarbunga"))
    print(count_vowels("grrrrgh!"))
    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_vowels("A nice day to code!"))
    print("---------------------------------")
    print("  ")
    print("Consonants in a string ")
    print("---------------------------------")
    print(count_consonants("Python"))
    print(count_consonants("Theistareykjarbunga"))
    print(count_consonants("grrrrgh!"))
    print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_consonants("A nice day to code!"))
    print("---------------------------------")
    print("  ")
    print("Char Histogram   ")
    print("---------------------------------")
    print(char_histogram("Python!"))
    print(char_histogram("AAAAaaa!!!"))
    print("---------------------------------")

    

        

