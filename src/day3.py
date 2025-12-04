from file_helpers import Lines, get_lines


def get_max_battery(batteries: str):
	li_batteries: list[int] = [int(c) for c in batteries]
	maximum: int = 0

	for i, battery in enumerate(li_batteries):
		for second_battery in li_batteries[i + 1:]:
			maximum = max(maximum, battery * 10 + second_battery)

	return maximum


def get_total_battery(lines: Lines):
	total: int = 0
	for line in lines:
		total += get_max_battery(line)

	return total


def main() -> None:
	file_input = get_lines(3)
	print(f'Part 1 = {get_total_battery(file_input)}')


if __name__ == '__main__':
	main()
