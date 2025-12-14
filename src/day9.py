from file_helpers import Lines, get_lines


type Index2D = tuple[int, int]


def get_indexes(lines: Lines) -> list[Index2D]:
	indexes: list[Index2D] = []

	for line in lines:
		temp: list[int] = [int(char) for char in line.split(',')]
		indexes.append((temp[0], temp[1]))

	return indexes


def get_largest_area(lines: Lines) -> int:
	indexes: list[Index2D] = get_indexes(lines)
	max_area: int = 0

	for i, (row, col) in enumerate(indexes):
		for row2, col2 in indexes[:i] + indexes[i + 1:]:
			max_area = max(max_area, (abs(row2 - row) + 1) * (abs(col2 - col) + 1))

	return max_area


"""
Validation functions based on implementation by nitekat1124
source: https://github.com/nitekat1124/advent-of-code-2025
"""

def get_largest_area_part_2(lines: Lines) -> int:
	indexes: list[Index2D] = get_indexes(lines)

	edges: list[tuple[Index2D, Index2D]] = [(indexes[i], indexes[(i + 1) % len(indexes)]) for i in range(len(indexes))]

	all_rects: list[tuple[int, Index2D, Index2D]] = []

	for i1, j1 in indexes:
		for i2, j2 in indexes:
			area = (abs(i1 - i2) + 1) * (abs(j1 - j2) + 1)
			all_rects.append((area, (i1, j1), (i2, j2)))

	all_rects.sort(reverse=True)


	def is_point_valid(point: Index2D) -> bool:
		j = len(indexes) - 1
		p1, p2 = point
		intersections = 0

		for i in range(len(indexes)):
			xi, yi = indexes[i]
			xj, yj = indexes[j]

			if min(xi, xj) <= p1 <= max(xi, xj) and min(yi, yj) <= p2 <= max(yi, yj):
				return True

			if xi == xj and min(yi, yj) <= p2 < max(yi, yj) and xi > p1:
				intersections += 1
			j = i
		return intersections % 2 == 1


	def is_crossing(side, edge):
		a, b = side
		c, d = edge

		#check direction
		if (a[0] == b[0] and c[0] == d[0]) or (a[1] == b[1] and c[1] == d[1]):
			return False

		#check if the lines cross
		if a[0] == b[0]:
			return  min(c[0], d[0]) < a[0] < max(c[0], d[0]) and min(a[1], b[1]) < c[1] < max(a[1], b[1])
		elif a[1] == b[1]:
			return min(c[1], d[1]) < a[1] < max(c[1], d[1]) and min(a[0], b[0]) < c[0] < max(a[0], b[0])
		return False

	def is_valid(start: Index2D, end: Index2D) -> bool:
		x1, y1 = start
		x2, y2 = end
		min_x, max_x = min(x1, x2), max(x1, x2)
		min_y, max_y = min(y1, y2), max(y1, y2)

		corners = [
			(min_x, min_y),
			(min_x, max_y),
			(max_x, max_y),
			(max_x, min_y)
		]

		for corner in corners:
			if not is_point_valid(corner):
				return False

		sides = [
			(corners[0], corners[1]),
			(corners[1], corners[2]),
			(corners[2], corners[3]),
			(corners[3], corners[0]),
		]

		for side in sides:
			for edge in edges:
				if is_crossing(side, edge):
					return False
		return True

	for area, z1, z2 in all_rects:
		if is_valid(z1, z2):
			return area

	return 0


def main() -> None:
	# file_input = get_lines(9, 'example_input.txt')
	file_input = get_lines(9)
	print(f'Part 1 = {get_largest_area(file_input)}')
	print(f'Part 2 = {get_largest_area_part_2(file_input)}')


if __name__ == '__main__':
	main()
