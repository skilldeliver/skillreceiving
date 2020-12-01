
def part_one(data):
    for i in range(len(data) - 1):
        for j in range(1, len(data)):
            if data[i] + data[j] == 2020:
                return data[i] * data[j]

def part_two(data):
    for i in range(len(data) - 2):
        for j in range(1, len(data) - 1):
            for k in range(2, len(data)):
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]

with open('inputs/day01.txt') as f:
    data = [int(line) for line in f.readlines()]

    print(part_one(data))
    print(part_two(data))
