
def part_one(data):
	return sum(i//3-2 for i in data)

def part_two(data):
	total = int()
	for entry in data:
		while (entry := entry//3-2) > 0:
			total += entry
	return total

with open('inputs/day01.txt') as f:
	data = [int(line) for line in f.readlines()]

	print(part_one(data))
	print(part_two(data))
