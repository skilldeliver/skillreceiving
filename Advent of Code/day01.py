"""
--- Day 1: Chronal Calibration ---

"""


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


def load_input(link):
    import urllib.request

    uf = urllib.request.urlopen(link)
    content = uf.readlines()

    return [line.decode('utf-8').strip('\r\n') for line in content]


if __name__ == '__main__':
    main()
