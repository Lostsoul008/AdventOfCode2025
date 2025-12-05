from file_helpers import Lines, get_lines


def get_fresh_id_count(lines: Lines) -> int:
	ranges: list[tuple[int, int]] = []
	ids: list[int] = []
	result: int = 0
	post_ranges: bool = False

	for line in lines:
		if not post_ranges:
			if line == '':
				post_ranges = True
				continue
			temp = line.split('-')
			ranges.append((int(temp[0]), int(temp[1])))
		else:
			ids.append(int(line))

	for available_id in ids:
		for start, end in ranges:
			if start <= available_id <= end:
				result += 1
				break

	return result


def main() -> None:
	file_input = get_lines(5, 'example_input.txt')
	file_input = get_lines(5)
	print(f'Part 1 = {get_fresh_id_count(file_input)}')


if __name__ == '__main__':
	main()
