from file_helpers import Lines, get_lines


def get_max_battery(batteries: str, total: int = 2):
	li_batteries: list[int] = [int(c) for c in batteries]
	length = len(batteries)
	start = 0
	result = 0

	while total > 0:
		total -= 1
		largest_digit = 0
		largest_index = 0

		for i in range(start, length - total):
			if li_batteries[i] > largest_digit:
				largest_digit = li_batteries[i]
				largest_index = i

		start = largest_index + 1
		result += 10 ** total * li_batteries[largest_index]

	return result


def get_total_battery(lines: Lines, total_bat: int = 2):
	total: int = 0
	for line in lines:
		total += get_max_battery(line, total_bat)

	return total


def main() -> None:
	file_input = get_lines(3)
	print(f'Part 1 = {get_total_battery(file_input)}')
	print(f'Part 2 = {get_total_battery(file_input, 12)}')


if __name__ == '__main__':
	main()
