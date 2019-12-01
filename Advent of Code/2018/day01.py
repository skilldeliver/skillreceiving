"""
--- Day 1: Chronal Calibration ---

"""
from utils import load_input


def main():
    lines = load_input('https://pastebin.com/raw/ebDxSugK')
    print(part_one(lines))
    print(part_two(lines))


def part_one(iterable):
    return sum([int(change) for change in iterable])


def part_two(iterable):
    changes = [int(i) for i in iterable]

    frequencies = set()
    current_frequency = int()

    while True:
        for change in changes:
            current_frequency += change
            if current_frequency in frequencies:
                return current_frequency
            frequencies.add(current_frequency)


if __name__ == '__main__':
    main()