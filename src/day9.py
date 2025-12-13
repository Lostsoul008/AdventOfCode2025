from file_helpers import Lines, get_lines


def get_largest_area(lines: Lines) -> int:
	indexes: list[tuple[int, int]] = []

	for line in lines:
		temp: list[int] = [int(char) for char in line.split(',')]
		indexes.append((temp[0], temp[1]))

	max_area: int = 0

	for i, (row, col) in enumerate(indexes):
		for row2, col2 in indexes[:i] + indexes[i + 1:]:
			max_area = max(max_area, (abs(row2 - row) + 1) * (abs(col2 - col) + 1))


	return max_area


def main() -> None:
	# file_input = get_lines(9, 'example_input.txt')
	file_input = get_lines(9)
	print(f'Part 1 = {get_largest_area(file_input)}')


if __name__ == '__main__':
	main()
