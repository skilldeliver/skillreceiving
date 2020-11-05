"""
--- Day 2: Inventory Management System ---
"""
import itertools
from utils import load_input


def main():
    lines = load_input('https://pastebin.com/raw/HSnu5ViM')
    print(part_one(lines))
    print(part_two(lines))


def part_one(iterable):
    two = three = bool()
    occurs = dict(two=0, three=0)

    for s in iterable:
        for l in s:
            if not two and s.count(l) == 2:
                two = True
            if not three and s.count(l) == 3:
                three = True
            if two and three:
                break

        occurs['two'] += two
        occurs['three'] += three
        two = three = bool()

    return occurs['two'] * occurs['three']


def part_two(iterable):
    result = str()
    for s1, s2 in itertools.combinations(iterable, 2):
        diffs = [i for i in range(len(s1)) if s1[i] != s2[i]]
        if len(diffs) == 1:
            for l in s1:
                if s1.index(l) not in diffs:
                    result += l
    return result


if __name__ == '__main__':
    main()
