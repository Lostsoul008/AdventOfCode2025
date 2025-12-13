from functools import cache

from file_helpers import Lines, get_lines


def count_splits(lines: Lines) -> int:
	height: int = len(lines)
	length: int = len(lines[0])
	all_splits: set[tuple[int, int]] = set()

	def count_splits_path(current_line: int, current_char: int) -> None:
		for i in range(current_line, height):
			if lines[i][current_char] == '^':

				if (i, current_char) in all_splits:
					return
				all_splits.add((i, current_char))

				if current_char + 1 < length:
					count_splits_path(i + 1, current_char + 1)
				if current_char - 1 >= 0:
					count_splits_path(i + 1, current_char - 1)
				return
	count_splits_path(1, lines[0].index('S'))
	return len(all_splits)


def count_splits_part_2(lines: Lines) -> int:
	height: int = len(lines)
	length: int = len(lines[0])

	@cache
	def count_splits_path_part_2(current_line: int, current_char: int) -> int:
		for i in range(current_line, height):
			if lines[i][current_char] == '^':
				result: int = 0

				if current_char + 1 < length:
					result += count_splits_path_part_2(i + 1, current_char + 1)
				if current_char - 1 >= 0:
					result += count_splits_path_part_2(i + 1, current_char - 1)
				return result
		return 1

	all_quantum: int = count_splits_path_part_2(1, lines[0].index('S'))

	count_splits_path_part_2.cache_clear()
	return all_quantum


def main() -> None:
	# file_input = get_lines(7, 'example_input.txt')
	file_input = get_lines(7)
	print(f'Part 1 = {count_splits(file_input)}')
	print(f'Part 2 = {count_splits_part_2(file_input)}')


if __name__ == '__main__':
	main()
