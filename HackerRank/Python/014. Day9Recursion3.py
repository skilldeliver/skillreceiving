def factorial(n):
    if n > 1: return n * factorial(n - 1)
    else: return n

print(factorial(3)) 

# faster or maybe more correct for Hacker Rank
def factorial1(n):
    if n > 1: return factorial1(n - 1) * n
    else: return n

num = int(input())
print(factorial1(num))

def factorial2(number):
    if number <= 1:
        return 1
    else:
        return factorial2(number-1) * number
        
N = int(input())
print(factorial2(N))