from typing import List
from Helper.file_helpers import getLines


def get_ranges(lines: List[str]) -> List[tuple[int, int]]:
	ranges: List[tuple[int, int]] = []
	for line in lines:
		for range_pair in line.strip(',').split(','):
			range_pair_list = range_pair.split('-')
			if len(range_pair_list) == 2:
				ranges.append((int(range_pair_list[0]), int(range_pair_list[1])))

	return ranges


def get_invalid(ranges: List[tuple[int, int]]) -> List[int]:
	result: List[int] = []
	for start, end in ranges:
		for i in range(start, end + 1):
			str_i = str(i)
			length = len(str_i)
			mid = length // 2

			if length % 2 == 0 and str_i[:mid] == str_i[mid:]:
				result.append(i)

	return result


def sum_invalid(values: List[int]) -> int:
	return sum(values)


def main() -> None:
	file_input = getLines()
	print(f'{sum_invalid(get_invalid(get_ranges(file_input))) = }')


if __name__ == '__main__':
	main()
