from collections import Counter

with open("inputs/day04.txt") as f:
    lower, higher = map(int, f.readline().split("-"))
    scope = range(lower, higher)

    predicate_1 = lambda x: "".join(sorted(x)) == x and any(
        x == y for x, y in zip(x, x[1:])
    )
    predicate_2 = lambda x: "".join(sorted(x)) == x and any(
        v == 2 for v in Counter(x).values()
    )

    solve = lambda s, f: len(list(filter(f, [str(i) for i in s])))

    print('Part one:', solve(scope, predicate_1))
    print('Part two:', solve(scope, predicate_2))
