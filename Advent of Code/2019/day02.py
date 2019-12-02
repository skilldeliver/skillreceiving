
def part_one(source_data, noun, verb):
	data = source_data.copy()
	data[1], data[2] = noun, verb

	for i in range(0, len(data), 4):
		operator, a, b, dest = data[i:i+4]

		if operator == 1:
			data[dest] = data[a] + data[b]
		elif operator == 2:
			data[dest] = data[a] * data[b]
		elif operator == 99:
			break

	return data[0]


def part_two(source_data):
	for noun in range(99):
		for verb in range(99):
			if part_one(source_data, noun, verb) == 19690720:
				return 100 * noun + verb


with open('inputs/day02.txt') as f:
	source_data = [int(number) for number in f.readline().split(',')]
	print(part_one(source_data, 12, 2))
	print(part_two(source_data))
