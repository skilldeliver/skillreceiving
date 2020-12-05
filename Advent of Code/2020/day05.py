
def part_one(data, find_max=True):
    max_seat = 0
    seats = list()

    lower = lambda x: range(x.start, x.start+(len(x)//2))
    upper = lambda x: range(x.start+len(x)//2, x.stop)

    for seat in data:
        row, column = range(128), range(8)

        for char in seat:
            if char == 'F':
                row = lower(row) 
            elif char == 'B':
                row = upper(row)
            elif char == 'L':
                column = lower(column)
            elif char == 'R':
                column = upper(column)

        current = row.start*8+column.start

        if find_max:
            if current > max_seat:
                max_seat = current
        else:
            seats.append(current)
    return max_seat if find_max else seats


def part_two(data):
    seats = sorted(part_one(data, find_max=False))
    for i, j in zip(seats, seats[1:]):
        if j - i != 1:
            return i + 1

with open('inputs/day05.txt') as f:
    data = [line for line in f.readlines()]
    print(part_one(data))
    print(part_two(data))
