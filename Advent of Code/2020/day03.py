
def part_one(data, right, down):
    counter = 0
    x_pos = 0
    line_len = len(data[0])
    line_len = line_len - 1 if line_len % 2 == 0 else line_len

    for line in range(0, len(data), down):
        x_pos += right

        try:
            if data[line + down][x_pos % line_len] == "#":
                counter += 1
        except IndexError:
            break  
    return counter

def part_two(data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    result = 1

    for s in slopes:
        result *= part_one(data, *s)
    return result

with open('inputs/day03.txt') as f:
    data = [line for line in f.readlines()]
    print(part_one(data, 3, 1))
    print(part_two(data))
