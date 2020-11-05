k = int(input())
room_list = input()

room_arr = []
person_arr = []

for i in room_list:
    if i != " ":
        room_arr.append(int(i))
        
person = int((len(room_arr) - 1) / k)
for j in range(person, 0, -1):
    person_arr.append(j)
    
is_in = False
def main():
    for k in (room_arr):
        for l in person_arr:
            if (k == l):
                is_in = True
        if not is_in:
            print(k)
            return
        is_in = False
main()