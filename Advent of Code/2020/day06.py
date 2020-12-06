from string import ascii_lowercase

def part_one(data):
    total = 0
    for group in data:
        group_set = set()
        for person in group.split():
            for answer in person:
                group_set.add(answer)
        total += len(group_set)
    return total

def part_two(data):
    total = 0
    for group in data:
        group_set = set(list(ascii_lowercase))
        for person in group.split():
            answers = [a for a in person]
            group_set.intersection_update(set(answers))
        total += len(group_set)
    return total

def oneliner(data, part=1):
    return sum([len(set(a for p in g.split() for a in p)) for g in data]) if part == 1 else sum([len(set(list([chr(97+i) for i in range(26)])).intersection(*[set(a for a in p) for p in g.split()])) for g in data]) 

with open('inputs/day06.txt') as f:
    data = [p for p in f.read().split('\n\n')]
    print(oneliner(data))
    print(oneliner(data, part=2))
