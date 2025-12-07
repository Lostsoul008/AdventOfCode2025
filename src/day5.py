from typing import Optional

from file_helpers import Lines, get_lines


def get_fresh_id_count(lines: Lines, all_values: bool = False) -> int:
	ranges: list[tuple[int, int]] = []
	ids: list[int] = []
	result: int = 0
	post_ranges: bool = False

	for line in lines:
		if not post_ranges:
			if line == '':
				post_ranges = True
				if all_values:
					break
				else:
					continue
			temp = line.split('-')
			ranges.append((int(temp[0]), int(temp[1])))
		else:
			ids.append(int(line))

	if not all_values:
		for available_id in ids:
			for start, end in ranges:
				if start <= available_id <= end:
					result += 1
					break
	else:
		was_changed = True
		i = 0
		while was_changed:
			was_changed = False

			while i < len(ranges):

				cur_start, cur_end = ranges[i]
				to_add: Optional[tuple[int, int]] = None

				for j in range(i + 1, len(ranges)):
					other_start, other_end = ranges[j]

					if other_start <= cur_start <= other_end:
						if cur_end > other_end:
							to_add = (other_end + 1, cur_end)
						was_changed = True
						break

					if other_start <= cur_end <= other_end:
						if cur_start < other_start:
							to_add = (cur_start, other_start - 1)
						was_changed = True
						break

				if was_changed:
					ranges.pop(i)
					if to_add:
						ranges.append(to_add)
					break
				i += 1

		for start, end in ranges:
			result += end - start + 1

	return result


def main() -> None:
	file_input = get_lines(5)
	print(f'Part 1 = {get_fresh_id_count(file_input)}')
	print(f'Part 2 = {get_fresh_id_count(file_input, True)}')


if __name__ == '__main__':
	main()
