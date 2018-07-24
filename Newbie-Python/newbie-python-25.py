def anti_vowel(text):
    storeIn = ""
    for c in text:
        if c not in "aeiouAEIOU":
            storeIn += c
            return storeIn
         

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}







def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result





def count (sequence, item):
    count = 0
    for i in sequence:
        if type (item) != list:
            if i == item:
                count += 1
        else:
            for n in item:
                if n == i:
                    count += 1
    return count 




def purify(n):
    n_even=[]
    for i in n:
        if i%2==0:
            n_even.append(i)
    return n_even

'''
def product(n):
    n_all = []
    for i in n:
        if i > 0:
            c = i * i * i * i * i
            n_all.append(c)
    return int(n_all)'''


def product(numbers):
    total = 1
    for each in numbers:
        total *= each
    return total


def remove_duplicates(nimbs):
    noDup=[]
    marks={}
    for j in nimbs:
            marks[j]=False
    for i in nimbs:
        if marks[i]==False:
            noDup.append(i)
            marks[i]=True
    return noDup




a = 2 ** 32
print(a)









    
