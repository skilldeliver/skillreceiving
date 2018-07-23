
def is_number_balanced(number):
    snum = str(number)
    if len(snum) == 1: return True
    elif len(snum) % 2 == 0:
        return sum(int(snum[i]) for i in range(len(snum) // 2)) == sum(int(snum[j]) for j in range(len(snum) - 1, len(snum) // 2 - 1, -1))
    return sum(int(snum[i]) for i in range((len(snum) - 1) // 2)) == sum(int(snum[j]) for j in range(len(snum) - 1, len(snum) // 2, -1))

def increasing_or_decreasing(seq):

    up, down = 1, 1
    for i in range(len(seq) - 1):
        if not seq[i] < seq[i + 1]:
            up = False
        if not seq[i] > seq[i + 1]:
            down = 0

    if up: return "Up!"
    elif down: return "Down!"
    return up

def get_largest_palindrome(n):
    for i in range(n - 1, -1, -1):
        if str(i) == str(i)[::-1]: return i

def sum_of_numbers(input_string):
    n_str = ""
    total = 0
    for i in (input_string + " "):
        if i in "1234567890":
            n_str += i
        elif n_str:
            total += int(n_str)
            n_str = ""
        
    return total

def birthday_ranges(birthdays, ranges):
    


if __name__ == "__main__":
    print("1. Is Number Balanced?")
    print("--------------------------------")
    print(is_number_balanced(9))
    print(is_number_balanced(4518))
    print(is_number_balanced(28471))
    print(is_number_balanced(1238033))
    print("--------------------------------")
    print("    ")
    print("2. Increasing and Decreasing Sequences")
    print("--------------------------------")
    print(increasing_or_decreasing([1,2,3,4,5]))
    print(increasing_or_decreasing([5,6,-10]))
    print(increasing_or_decreasing([1,1,1,1]))
    print(increasing_or_decreasing([9,8,7,6]))
    print("--------------------------------")
    print("    ")
    print("3. Largest Palindrome")
    print("--------------------------------")
    print(get_largest_palindrome(99))
    print(get_largest_palindrome(252))
    print(get_largest_palindrome(994687))
    print(get_largest_palindrome(754649))
    print("--------------------------------")
    print("    ")
    print("4. Sum all numbers in a given string")
    print("--------------------------------")
    print(sum_of_numbers("ab125cd3"))
    print(sum_of_numbers("ab12"))
    print(sum_of_numbers("ab"))
    print(sum_of_numbers("1101"))
    print(sum_of_numbers("1111O"))
    print(sum_of_numbers("1abc33xyz22"))
    print(sum_of_numbers("0hfabnek"))
    print("--------------------------------")
    print("    ")
    print("5. Birthday Ranges")
    print("--------------------------------")









