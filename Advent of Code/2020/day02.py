
def part_one(data):
    valid_passwords = 0

    for line in data:
        tokens = line.split()
        
        occur = [int(i) for i in tokens[0].split('-')]
        char = tokens[1][0]
        password = tokens[2]

        if occur[0] <= password.count(char) <= occur[1]:
            valid_passwords += 1
    return valid_passwords

def part_two(data):
    valid_passwords = 0

    for line in data:
        tokens = line.split()
        
        occur = [int(i) for i in tokens[0].split('-')]
        char = tokens[1][0]
        password = tokens[2]
        match = [o for o in occur if password[o-1] == char]

        if len(match) == 1:
            valid_passwords += 1
    return valid_passwords

with open('inputs/day02.txt') as f:
    data = [line for line in f.readlines()]

    print(part_one(data))
    print(part_two(data))
