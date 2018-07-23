n = int(input())
dict_phones = {}
 
for i in range(n):
    name_phone = input().split()
    dict_phones[name_phone[0]] = name_phone[1]
 
for i in range(n):
    name = input();
     
    if name in dict_phones:
        print(name + "=" + dict_phones[name])
    else:
        print("Not found")