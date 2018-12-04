import timeit
import re
from datetime import datetime as dt
from collections import namedtuple

from utils import load_input


def main():
    lines = load_input('https://pastebin.com/raw/VdZiDjRn')
    guards, ans = part_one(lines)

    print(part_two(guards))


def part_one(iterable):
    p = r'\[(.*)\] (Guard #\d*)?(.*)'

    records = list()
    Record = namedtuple('Record', 'time guard action')

    for line in iterable:
        m = re.match(p, line)
        time = dt.strptime(m.group(1), '%Y-%m-%d %H:%M')
        guard = None if not m.group(2) else m.group(2)[7:]
        action = m.group(3)
        records.append(Record(time, guard, action))

    records.sort(key=lambda r: r.time)
    guards = dict()
    guard = str()

    asleep = awake = int()

    for record in records:
        if record.guard:
            guard = record.guard
        if guard not in guards.keys():
            guards[guard] = list()

        if record.action == 'falls asleep':
            asleep = record.time.minute
        elif record.action == 'wakes up':
            awake = record.time.minute

        if asleep and awake:
            guards[guard].append(set(range(asleep, awake)))
            asleep = awake = int()

    more = {'k': str(), 'sum': int()}
    for k, v in guards.items():
        csum = sum(1 for r in v for i in r)

        if csum > more['sum']:
            more['sum'] = csum
            more['k'] = k

    minutes = [0 for _ in range(60)]

    for s in guards[more['k']]:
        for i in s:
            minutes[i] += 1

    minute = minutes.index(max(minutes))
    return guards, (minute + 2) * int(more['k'])


def part_two(guards):
    most_asleep = [str(), int(), int()]

    for k, v in guards.items():
        minutes = [0 for _ in range(60)]
        for s in v:
            for i in s:
                minutes[i] += 1
        minute = max(minutes)

        if minute > most_asleep[1]:
            most_asleep = [k, minute, minutes.index(minute)]

    return int(most_asleep[0]) * most_asleep[2]


if __name__ == '__main__':
    main()
