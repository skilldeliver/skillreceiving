
def anagrams(word_1, word_2):
    list1 = list(word_1.lower())
    list2 = list(word_2.lower())
    list1.sort()
    list2.sort()
    if list1 == list2:
        return "ANAGRAMS"
    return "NOT ANAGRAMS"

w1, w2 = input().split()
print(anagrams(w1, w2))