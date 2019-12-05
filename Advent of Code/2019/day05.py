def part_one(source_data):

	data = source_data.copy()
	i = 0

	while i < len(data):
		operator = str(data[i]).zfill(5)
		# print('OPERATOR: ', operator)

		if int(operator[-1]) in (1, 2):
			opcode = int(operator[-1])
			dest = data[i+3]

			a = data[data[i+1]] if operator[-3] == '0' else data[i+1]
			b = data[data[i+2]] if operator[-4] == '0' else data[i+2]

			if opcode == 1:
				data[dest] = a + b
			elif opcode == 2:
				data[dest] = a * b

			i += 4

		elif int(operator[-1]) in (3, 4):
			opcode = int(operator[-1])
			dest = data[i+1]	

			if opcode == 3:
				data[dest] = int(input())
			elif opcode == 4:
				print(data[dest])
			i += 2

		elif int(operator[-1]) in (5, 6, 7, 8):
			opcode = int(operator[-1])
			print(opcode)

			if opcode == 5:
				a = data[data[i+1]] if operator[-3] == '0' else data[i+1]
				b = data[data[i+2]] if operator[-4] == '0' else data[i+2]

				if a != 0:
					i = b
				else:
					i += 3

			elif opcode == 6:
				a = data[data[i+1]] if operator[-3] == '0' else data[i+1]
				b = data[data[i+2]] if operator[-4] == '0' else data[i+2]

				if a == 0:
					i = b
				else:
					i += 3

			elif opcode == 7:
				dest = data[i+3]

				a = data[data[i+1]] if operator[-3] == '0' else data[i+1]
				b = data[data[i+2]] if operator[-4] == '0' else data[i+2]
				c = data[data[i+3]] if operator[-5] == '0' else data[i+3]

				if a < b:
					data[c] = 1
				else:
					data[c] = 0

				i += 4

			elif opcode == 8:
				dest = data[i+3]

				a = data[data[i+1]] if operator[-3] == '0' else data[i+1]
				b = data[data[i+2]] if operator[-4] == '0' else data[i+2]
				c = data[data[i+3]] if operator[-5] == '0' else data[i+3]

				if a == b:
					data[c] = 1
				else:
					data[c] = 0

				i += 4


		elif int(operator[-2:]) == 99:
			break

	return data[0]


with open('inputs/day05.txt') as f:
	source_data = [int(number) for number in f.readline().split(',')]
	print(part_one(source_data))
