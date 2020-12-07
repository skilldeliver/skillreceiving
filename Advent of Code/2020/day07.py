def part_one(data):
    bags = dict()

    for l in data:
        bag, contains = l.split(' contain ')
        bag = '-'.join([i for i in bag.split(' ')[:2]])
        contains = ['-'.join([j for j in (i.split()[1:3])]) for i in contains.split(', ') if not i.startswith('no')]
        bags[bag] = contains

    finished = False
    tokens = ['shiny-gold']
    count = 0
    all_bags = []
    while not finished:
        new_tokens = list()
        for key, value in bags.items():
            if len([1 for t in tokens if t in value]) >= 1:
                new_tokens.append(key)
                count += 1
        if len(new_tokens) == 0:
            finished = True
        tokens = list(set(new_tokens))
        all_bags.append(new_tokens)
    return count

def part_two(data):
    pass

with open('inputs/day07.txt') as f:
    data = [p for p in f.read().split('\n')]
    print(part_one(data))
    print(part_two(data))
