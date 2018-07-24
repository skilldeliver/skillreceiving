import os
total_lines = 0

for i in range(1, 141):
    if i != 138:
        file = open("newbie-python-" + str(i) + ".py", "r", encoding="utf8")
        total_lines += len(file.readlines())
        file.close()
        
print(total_lines)