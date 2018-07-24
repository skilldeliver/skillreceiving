



def digit_int(n):
    first = n % 10
    ape1 = n // 10
    second = ape1 % 10
    ape2 = ape1 // 10
    third = ape2 % 10
    ape3 = ape2 // 10
    fourth = ape3 % 10
    ape4 = ape3 // 10
    fifth = ape4 % 10
    ape5 = ape4 // 10
    sixth = ape5 % 10
    ape6 = ape5 // 10
    seventh = ape6 % 10
    ape7 = ape6 // 10

    total = first + second + third + fourth + fifth + sixth + seventh + ape7
    print(total)
    return total


''' dont do factorials like this: :D :D :D :D :D    
def factorial(x):
    if x > 0:
        a = x - 1
    if a > 0:
        b = a - 1
    if b > 0:
        c = b - 1
    if c > 0:
        d = c - 1
    if d > 0:
        e = d - 1
   

    total = x * a * b * c * d * e
    print(total)
    return total '''

#real factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

''' fail again, but dont give up
def is_prime(x):
    for n in range(2, x - 1):
      if x % n == 0:
        print("Its not prime")
        return False
      else:
          print("Its prime")
          return True
'''

#real prime function
def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True


def isit_prime(x):
    if x < 2:
        print("It is not a prime number")
        return False
    else:
        for n in range(2, x - 1):
            if x % n == 0:
                print("It is not a prime number")
                return False
        print("It is a prime number")
        return True


def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word



reverse(abcdfghjkl)




























  
  
