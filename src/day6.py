import re
from typing import Callable
from file_helpers import Lines, get_lines


def mult(a, b):
	return a * b


def add(a, b):
	return a + b


def calculate_sum_columns(lines: Lines) -> int:
	operations: list[str] = re.split(r'\s+', lines[-1].strip())
	columns: list[list[int]] = [[int(val) for val in re.split(r'\s+', line.strip())] for line in lines[:-1]]

	result: int = 0
	for j in range(len(columns[0])):
		operation: Callable[[int, int], int] = mult if operations[j] == '*' else add
		temp = 1 if operations[j] == '*' else 0
		for i in range(len(columns)):
			temp = operation(temp, columns[i][j])

		result += temp

	return result


def main() -> None:
	# file_input = get_lines(6, 'example_input.txt')
	file_input = get_lines(6)
	print(f'Part 1 = {calculate_sum_columns(file_input)}')


if __name__ == '__main__':
	main()
