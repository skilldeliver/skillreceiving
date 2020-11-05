from time import time

class Line:
	def __init__(self, x1, y1, x2, y2, prev, distance=0):
		self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
		self.prev = prev
		self.distance = distance
		self.horizontal = self.y1 == self.y2

	@staticmethod
	def intersect(l1, l2):
		if l1.horizontal != l2.horizontal:
			hor = l1 if l1.horizontal else l2
			ver = l1 if not l1.horizontal else l2

			in_range_y = lambda a, b: min(a.y1, a.y2) <= b.y1 <= max(a.y1, a.y2)
			in_range_x = lambda a, b: min(a.x1, a.x2) <= b.x1 <= max(a.x1, a.x2)

			if in_range_y(ver, hor) and in_range_x(hor, ver):
				return (ver.x1, hor.y1)
		return False

def solve(wire_1_dirs, wire_2_dirs):
	lines = list()
	x = y = 0

	operations = {'R': lambda x, y, d: (Line(x+1, y , x+d, y, (x, y), d), x+d, y),
				  'L': lambda x, y, d: (Line(x-d, y, x, y, (x, y), d), x-d, y),
				  'U': lambda x, y, d: (Line(x, y, x, y+d, (x, y), d), x, y+d),
				  'D': lambda x, y, d: (Line(x, y-d, x, y, (x, y), d), x, y-d)
				}

	for item in wire_1_dirs:
		direction, distance = item[0], int(item[1:])
		line, x, y = operations[direction](x, y, distance)
		lines.append(line)

	x = y = cur_dist = 0
	intersects, min_dist = list(), 1000000000

	for item in wire_2_dirs:
		direction, distance, dist_here = item[0], int(item[1:]), 0
		line, x, y = operations[direction](x, y, distance)
		cur_dist += distance

		for l in lines:
			dist_here += l.distance

			if (intersect := Line.intersect(l, line)):
				dist_here -= l.distance
				cur_dist -= distance

				dist_here += abs(intersect[0] - l.prev[0]) + abs(intersect[1] - l.prev[1])
				cur_dist += abs(intersect[0] - line.prev[0]) + abs(intersect[1] - line.prev[1])

				if dist_here + cur_dist < min_dist:
					min_dist = dist_here + cur_dist
				intersects.append(intersect)

	return min([abs(i[0]) + abs(i[1]) for i in intersects]), min_dist

with open('inputs/day03.txt') as f:

	s = time()
	line_1, line_2 = f.readlines()
	wire_1_dirs = [d.strip() for d in line_1.split(',')]
	wire_2_dirs = [d.strip() for d in line_2.split(',')]

	print(len(wire_1_dirs), len(wire_2_dirs))
	# print(solve(wire_1_dirs, wire_2_dirs))
	e = time()
	print(1000 * (e - s))