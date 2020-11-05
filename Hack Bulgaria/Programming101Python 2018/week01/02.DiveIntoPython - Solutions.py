def count_substrings(haystack, needle):
    arr = [i for i in haystack]

    string, count = "", 0

    for i in range(len(arr)):
        string += arr[i]
        if needle in string:
            count += 1
            string = ""
            del arr[i - len(string):i]

    return count

def sum_matrix(m):
    return sum(j for i in m for j in i)

def nan_expand(n):
    out = ""
    
    for i in range(n):
        out += "Not a "
        if i == n - 1: out += "NaN"
    return out

def prime_factorization(n):
    primes = [i for i in range(2, 100) if all(i % j != 0 for j in range(2, i))]

    for i in primes:
        for j in primes:
            for k in range(0, 10):
                for l in range(0, 10):
                    if j ** l == n:
                        return [(j, l)]
                    elif (i ** k) * (j ** l) == n:
                        return [(i, k), (j, l)]

def max_consecutive(items):
    
    cur, max_con = 1, 0
    for i in range(1, len(items)):
        if items[i] == items[i - 1]: cur += 1
        else:
            if cur > max_con: max_con = cur
            cur = 1
    
    if cur > max_con: max_con = cur
    return max_con

def word_counter(word, arr, row, col):
    """ WORKING ONLY WITH EQUAL ROWS AND COLS OR WHEN COLS ARE > THAN THE ROWS """
    # Sorry, this is my best for now
    string = ""
    count = 0
    last_index = [[],[]]


# ~~~~~~~~~~~~~~~~ HORIZONTAL PART ~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~ LEFT TO RIGT ~~~~~~~~~~~~~~~~~~~~~~~

    for r in range(row):
        for c in range(col):
            string += arr[r][c]
            if word in string:
                last_index[0].append(r)
                last_index[1].append(c)
                count += 1
                string = ""
        string = ""
    string = ""

# ~~~~~~~~~~~~~~~~ RIGHT TO LEFT ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    for r in range(row):
        for c in range(col - 1, -1, -1):
            string += arr[r][c]
            if word in string:
                if r not in last_index[0] and c not in last_index[1]:
                    count += 1
                    string = ""
        string = ""
    string = ""
    

# # ~~~~~~~~~~~~~ VERTICAL PART ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    last_index = [[],[]]

# # ~~~~~~~~~~~~~~ FROM TOP TO BOTTOM ~~~~~~~~~~~~~~~~~~~~~~
    for c in range(col):
        for r in range(row):
            string += arr[r][c] 
            if word in string:
                last_index[0].append(r)
                last_index[1].append(c)
                count += 1
                string = ""
        string = ""
    string = ""
# # ~~~~~~~~~~~~~ FROM BOTTOM TO TOP ~~~~~~~~~~~~~~~~~~~~~~~
    for c in range(col):
        for r in range(row - 1, -1, -1):
            string += arr[r][c]
            if word in string:
                if r not in last_index[0] and c not in last_index[1]:
                    count += 1
                    string = ""
        string = ""
    string = ""

# # ~~~~~~~~~~~~ DIAGONAL PART ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# ~~~~~~~~~~~~~ TOP TO BOTTOM - LEFT TO RIGHT DIAGONAL ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    last_index = [[],[]]

#  ~~~~~~~~~~~~ TOP RIGHT PART - FROM TOP TO BOTTOM ~~~~~~~~~~~~~~~~~~~ or from left to right if u want
    diag_row = row
    angle = False
    if row > col:
        angle = True
    for c in range(col):
        if angle:
            diag_row -= 1
        for r in range(diag_row):
            string += arr[r][r + c]
            if r + c == col - 1 and r == row - 1: angle = True
            if word in string:
                last_index[0].append(r)
                last_index[1].append(c)
                count += 1
                string = ""
        #print(string)
        string = ""


#  ~~~~~~~~~~~~ TOP RIGHT PART - FROM BOTTOM TO TOP ~~~~~~~~~~~~~~~~~~~ or from right to left if u want
    diag_row = row
    angle = False
    if row > col:
        angle = True
    for c in range(col):
        if angle:
            diag_row -= 1
        for r in range(diag_row - 1, -1, -1):
            string += arr[r][r + c]
            if r + c == col - 1 and r == row - 1: angle = True
            if word in string:
                if r not in last_index[0] and c not in last_index[1]:
                    count += 1
                    string = ""
        #print(string)
        string = ""

# ~~~~~~~~~~ BOTTOM LEFT PART - FROM TOP TO BOTTOM ~~~~~~~~~~~~~~~~~~~~~~ or from left to right if u want
    last_index = [[],[]]

    diag_row = row
    for r in range(1, row):
        diag_row -= 1
        for c in range(diag_row):
            string += arr[r + c][c]
            if word in string:
                last_index[0].append(r)
                last_index[1].append(c)
                count += 1
                string = ""
        string = ""


# ~~~~~~~~~~ BOTTOM LEFT PART - FROM BOTTOM TO TOP ~~~~~~~~~~~~~~~~~~~~~~ or from right to left if u want
    diag_row = row
    for r in range(1, row):
        diag_row -= 1
        for c in range(diag_row - 1, -1, -1):
            string += arr[r + c][c]
            if word in string:
                if r not in last_index[0] and c not in last_index[1]:
                    count += 1
                    string = ""
        string = ""

# # ~~~~~~~~~~~~~ BOTTOM TO TOP - LEFT TO RIGHT DIAGONAL ~~~~~~~~~~~~~~~~~~~~~~~~~~~
    last_index = [[],[]]
# ~~~~~~~~~~~~ TOP LEFT PART - FROM LEFT TOP RIGHT ~~~~~~~~~~~~~~~~~~~~~ or from bottom to top if you want

    diag_row = row + 1
    for r in range(row - 1, -1, -1):
        diag_row -= 1
        for c in range(diag_row): 
            string += arr[r - c][c]
            if word in string:
                last_index[0].append(r)
                last_index[1].append(c)
                count += 1
                string = ""
        #print(string)
        string = ""
    string = ""

# ~~~~~~~~~~~~ TOP LEFT PART - FROM RIGHT TOP LEFT ~~~~~~~~~~~~~~~~~~~~~ or from top to bottom if you want
    diag_row = row + 1
    for r in range(row - 1, -1, -1):
        diag_row -= 1
        for c in range(diag_row): 
            string += arr[c][r - c]
            if word in string:
                if r not in last_index[0] and c not in last_index[1]:          
                    count += 1
                    string = ""
        #print(string)
        string = ""
    string = ""

# ~~~~~~~~~~~~ BOTTOM RIGHT PART - FROM LEFT TO RIGHT ~~~~~~~~~~~~~~~~~~~ or from bottom to top if u want
    last_index = [[],[]]
    angle = False
    if row == col:
        angle = True
    diag_row = row
    stop = -1
    for c in range(1, col):
        if angle:
            stop += 1
        for r in range(diag_row - 1, stop, -1):
            string += arr[r][((row - 1)- r) + c]
            if ((row - 1)- r) + c == col - 1 and r == 0: angle = True
            if word in string:
                last_index[0].append(r)
                last_index[1].append(c)
                count += 1
                string = ""
        #print(string)
        string = ""

    diag_row = row
    for r in range(1, row):
        diag_row -= 1
        for c in range(diag_row):
            string += arr[r + c][(col - 1) - c]
            if word in string:
                if r not in last_index[0] and c not in last_index[1]:          
                    count += 1
                    string = ""
        string = ""

    string = ""


    return count

def gas_stations(distance, tank_size, stations):
    km = tank_size
    path_arr = []
    arr = []

    while km < distance:
        path_arr.append(km)
        km += tank_size
    path_arr.append(distance)

    least = distance
    shortest = 0
    for i in path_arr:
        for j in stations:
            if i > j and i - j < least:
                least = i - j
                shortest = j
        arr.append(shortest)
        least = distance

    return arr
        




if __name__ == "__main__":                                                          
    print("Counting substrings")                            
    print("------------------------")                                                                                                                               
    print(count_substrings("This is a test string", "is"))                                                                                                                                                         
    print(count_substrings("babababa", "baba"))                                                                                                                                                                         
    print(count_substrings("Python is an awesome language to program in!", "o"))                                                                                                                                
    print(count_substrings("We have nothing in common!", "really?"))                                                                                                                                
    print(count_substrings("This is this and that is this", "this"))                                                                                                                                                                
    print("------------------------")                                                                                                                                                               
    print("  ")                                                                                                                                     
    print("Sum Numbers in Matrix")                                                          
    print("------------------------")                                       
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]   
    print(sum_matrix(m))                                                
    m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]                                               
    print(sum_matrix(m))                                                    
    m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]                                           
    print(sum_matrix(m))                                        
    print("------------------------")                                               
    print("  ")                                                                         
    print("NaN Expand")                                                 
    print("------------------------")                               
    print(nan_expand(0))                                        
    print(nan_expand(1))                                                                                                    
    print(nan_expand(2))                                                                                                            
    print(nan_expand(3))
    print("------------------------")
    print("  ")
    print("Integer prime factorization")
    print("------------------------")
    print(prime_factorization(10))
    print(prime_factorization(14))
    print(prime_factorization(356))
    print(prime_factorization(89))
    print(prime_factorization(1000))
    print("------------------------")
    print("  ")
    print("Longest subsequence of equal consecutive elements")
    print("------------------------")
    print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
    print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
    print("------------------------")
    print("  ")
    print("Word counter")
    print("------------------------")
    word = input()
    valid = 1
    row, col = input().split()

    if len(word) > int(row) or len(word) > int(col):
        valid = 0

    if valid:
        arr = [input().split() for i in range(int(row))]
        print(word_counter(word, arr, int(row), int(col)))
    else:
        print("Invalid number of rows or columns!")
    print("------------------------")
    print("  ")
    print("Gas Stations")
    print("------------------------")
    print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
    print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
    print("------------------------")

