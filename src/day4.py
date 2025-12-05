from file_helpers import get_lines, Lines


ROLL_CHARACTER = '@'
ROLL_CUTOFF = 4
PLACEHOLDER_CHARACTER = 'X'


def count_available_rolls(lines: Lines, can_remove: bool = False):
	x_max: int = len(lines)
	y_max: int = len(lines[0])
	result: int = 0

	def check_surrounding(x: int, y: int) -> bool:
		nearby_count: int = 0
		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 and j == 0:
					continue

				shift_x = x + i
				shift_y = y + j

				if shift_x < 0 or shift_x >= x_max or shift_y < 0 or shift_y >= y_max:
					continue

				if lines[shift_x][shift_y] == ROLL_CHARACTER:
					nearby_count += 1

		return nearby_count < ROLL_CUTOFF

	found: bool = True
	while found:
		found = False
		for row in range(x_max):
			for col in range(y_max):
				char = lines[row][col]
				if char == ROLL_CHARACTER and check_surrounding(row, col):
					if can_remove:
						lines[row] = lines[row][:col] + PLACEHOLDER_CHARACTER + lines[row][col + 1:]
						found = True
					result += 1

	return result


def main() -> None:
	# file_input = get_lines(4, 'example_input.txt')
	file_input = get_lines(4)

	print(f'Part 1: {count_available_rolls(file_input)}')
	print(f'Part 1: {count_available_rolls(file_input, True)}')

if __name__ == '__main__':
	main()
