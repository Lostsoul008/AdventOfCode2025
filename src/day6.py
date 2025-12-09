import re
from typing import Callable
from file_helpers import Lines, get_lines


def mult(a, b) -> int:
	return a * b


def add(a, b) -> int:
	return a + b


def dummy(a, b) -> int:
	return 0


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


def calculate_sum_columns_part2(lines: Lines) -> int:
	current_operation: Callable[[int, int], int] = dummy
	previous_start = 0
	result: int = 0

	for cur_index, char in enumerate(lines[-1]):
		if char == '*' or char == '+' or cur_index == len(lines[-1]) - 1:
			if current_operation == dummy:
				current_operation = mult if char == '*' else add
				previous_start = cur_index
				continue

			temp_index = cur_index + 1 if cur_index == len(lines[-1]) - 1 else cur_index - 1
			temp: list[str] = [''] * (temp_index - previous_start)
			for i in range(previous_start, temp_index):
				for j, line in enumerate(lines[:-1]):
					temp[i - previous_start] += line[i]


			temp_result: int = 1 if current_operation is mult else 0
			for value in [int(a.strip(' ')) for a in temp]:
				temp_result = current_operation(temp_result, value)

			current_operation = mult if char == '*' else add
			previous_start = cur_index

			result += temp_result

	return result


def main() -> None:
	# file_input = get_lines(6, 'example_input.txt')
	file_input = get_lines(6)
	print(f'Part 1 = {calculate_sum_columns(file_input)}')
	print(f'Part 2 = {calculate_sum_columns_part2(file_input)}')


if __name__ == '__main__':
	main()
