
def part_one(data):
    fields = ['byr','iyr','eyr','hcl','hgt','ecl','pid','cid']
    valid_count = 0

    for passport in data:
        curr = [t.split(':')[0] for t in passport.split()]
        if 'cid' in curr:
            curr.remove('cid')
        if sorted(curr) == sorted(fields[:-1]):
            valid_count += 1
    return valid_count

def part_two(data):
    valid_count = 0

    rules = {
        'byr': lambda n: 1920 <= int(n) <= 2002,
        'iyr': lambda n: 2010 <= int(n) <= 2020,
        'eyr': lambda n: 2020 <= int(n) <= 2030,
        'hgt': lambda s: {'cm': 150 <= int(s[:-2]) <= 193,
                          'in': 59 <= int(s[:-2]) <= 76}[s[-2:]],
        'hcl': lambda s: len(s) == 7 and int(s.strip('#'), base=16) >= 0,
        'ecl': lambda s: s in ('amb','blu','brn','gry','grn','hzl','oth'),
        'pid': lambda s: len(s) == 9 and all(c.isdigit() for c in s)
    }

    for passport in data:
        curr = {t.split(':')[0]:t.split(':')[1] for t in passport.split()}
        if 'cid' in curr:
            del curr['cid']
        if sorted(curr.keys()) != sorted(rules.keys()):
            continue

        all_valid = True    
        for k, v in curr.items():
            try:
                if not rules[k](v):
                    all_valid = False
                    break
            except:
                all_valid = False
                break
        if all_valid:
            valid_count += 1 
    return valid_count


with open('inputs/day04.txt') as f:
    data = [p for p in f.read().split('\n\r')]
    print(part_one(data))
    print(part_two(data))
