
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
    return [sum(1 for j in birthdays if j >= i[0] and j <= i[1]) for i in ranges]

def numbers_to_message(pressed_sequence):
    keys = [[" "], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]

    string = ""
    caps = False
    c = 0
    pressed_sequence.append(0)

    for i in range(len(pressed_sequence)):
        el = pressed_sequence[i]
        if el == 1: 
            caps = True
        elif el == 0:
            string += keys[el][el]
        elif el == -1:
            pass
        else:
            if el == pressed_sequence[i + 1]:
                c += 1
            else:
                if c >= len(keys[el]):
                    c -= (c // len(keys[el])) * len(keys[el])
                if caps:
                    string += keys[el][c].upper()
                    caps = False
                else:
                    string += keys[el][c]
                c = 0

    return string

def message_to_numbers(message):
    arr = []
    keys = [[" "], [], ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r", "s"], ["t", "u", "v"], ["w", "x", "y", "z"]]

    last_item = "*"
    for i in message:
        for el in keys:
            if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
                i = i.lower()
                arr.append(1)
            if i in el:
                if len(arr) > 0 and last_item in el:
                    arr.append(-1)
                for _ in range(el.index(i) + 1):
                    arr.append(keys.index(el))
        last_item = i

    return arr

def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):

    if not people_weight or not people_floors:
        return 0

    # I'll leave this problem because I think it is poorly explained
    # I need more time to decrypt it than to solve it
    # What is one elevator trip - does this include the return of the elevator for instance?
    # Maximum weight, icluding or not?

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
    print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
    print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))
    print("--------------------------------")
    print("    ")
    print("6. 100 SMS")
    print("--------------------------------")
    print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
    print(numbers_to_message([2, 2, 2, 2]))
    print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))
    print("--------------------------------")
    print("~~~~~~~~~~ reverse ~~~~~~~~~~~~~")
    print(message_to_numbers("abc"))
    print(message_to_numbers("Ivo e Panda"))
    print(message_to_numbers("aabbcc"))
    print("    ")
    print("7. Elevator Trips")
    print("--------------------------------")
    print(elevator_trips([], [], 5, 2, 200))
    print(elevator_trips([40, 50], [], 5, 2, 200))
    #print(elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200))
    #print(elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200))
    print("--------------------------------")
    
