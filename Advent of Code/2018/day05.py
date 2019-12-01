from utils import load_input
import timeit


def main():
    pass
    # print(part_one(string, combs))
    # print(part_two(string))


def part_one(string, combos):
    changing = True

    while changing:
        old_string = string
        for combo in combos:
            string = string.replace(combo, '')
        if len(string) == len(old_string):
            changing = False

    return len(old_string)


def part_two(string):
    lets = 'qwertyuiopasdfghjklzxcvbnm'
    small = 99999999

    for l in lets:
        curr = part_one(string.replace(l, '').replace(l.upper(), ''), combos())
        if curr < small:
            small = curr
    return small


def combos():
    combs = set()
    lets = 'qwertyuiopasdfghjklzxcvbnm'

    for l in lets:
        combs.add(f'{l}{l.upper()}')
    for l in lets.upper():
        combs.add(f'{l}{l.lower()}')
    return combs

string = load_input('https://pastebin.com/raw/TpG550mX', as_string=True)
combs = combos()

print(timeit.timeit('part_one(string, combs)', globals=globals(), number=1000))

# if __name__ == '__main__':
#     main()
