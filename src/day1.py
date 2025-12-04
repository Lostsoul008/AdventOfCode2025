from file_helpers import Lines, get_lines

MAX_ROTATION: int = 100
START_POS: int = 50
ROTATION: dict[str, int] = {
	'L': -1,
	'R': 1
}

def get_password(lines: Lines) -> int:
	password: int = 0
	current_rotation: int = START_POS
	line: str
	for line in lines:
		current_rotation = (current_rotation + int(line[1:]) * ROTATION[line[0]]) % MAX_ROTATION
		if current_rotation == 0:
			password += 1
			
	return password


def get_password_new_method(lines: Lines) -> int:
	password: int = 0
	current_rotation: int = START_POS
	line: str
	for line in lines:
		direction: int = ROTATION[line[0]]
		to_rotate: int = int(line[1:])

		if direction == 1:
			password += (current_rotation + to_rotate) // MAX_ROTATION
		else:
			invert_rotation = (MAX_ROTATION - current_rotation) % MAX_ROTATION
			password += (invert_rotation + to_rotate) // MAX_ROTATION

		current_rotation = (current_rotation + int(line[1:]) * ROTATION[line[0]]) % MAX_ROTATION

	return password


def main() -> None:
	file_input: Lines = get_lines(1)
	print(f'Part 1 = {get_password(file_input)}')
	print(f'Part 2 = {get_password_new_method(file_input)}')


if __name__ == '__main__':
	main()
