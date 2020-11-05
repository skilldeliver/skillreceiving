
a = [2, 4]
b = [16, 32, 96]

new_arr = []
factors = []
final = []
let_in = 1

for i in range(1, b[0] + 1):
    for num in a:
        if i % num != 0: let_in = 0
    if let_in: factors.append(i)
    let_in = 1
    

for el in factors:
    for num in b:
        if num % el != 0: let_in = 0
    if let_in: final.append(el)
    let_in = 1

print(len(final))