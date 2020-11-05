import re
from collections import namedtuple

from utils import load_input


def main():
    lines = load_input('https://pastebin.com/raw/qmUQ2B4a')
    squrs, rects, ans = part_one(lines)

    print(ans)
    print(part_two(squrs, rects))


def part_one(iterable):
    Rectangle = namedtuple('Rectangle', 'x y x1 y1')
    pattern = r'^#(\d{1,4}) @ (\d{1,3}),(\d{1,3}): (\d{1,3})x(\d{1,3})$'

    rectangles = dict()
    squares = dict()

    for line in iterable:
        match = re.search(pattern, line)
        ID, x, y, w, h = map(int, match.groups())

        rect = Rectangle(x, y, x + w, y + h)
        rectangles[ID] = rect

        for x in range(rect.x, rect.x1):
            for y in range(rect.y, rect.y1):
                key = f'{x}|{y}'
                if key in squares.keys():
                    squares[key] += 1
                else:
                    squares[key] = 1

    ans = len([1 for k in squares if squares[k] > 1])
    return squares, rectangles, ans


def part_two(squares, rectangles):
    for k, v in rectangles.items():
        rect_squares = list()
        for x in range(v.x, v.x1):
            for y in range(v.y, v.y1):
                rect_squares.append(squares[f'{x}|{y}'] == 1)
        if all(rect_squares):
            return k

if __name__ == '__main__':
    main()
