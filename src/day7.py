
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


def main() -> None:
	# file_input = get_lines(7, 'example_input.txt')
	file_input = get_lines(7)
	print(f'Part 1 = {count_splits(file_input)}')


if __name__ == '__main__':
	main()
