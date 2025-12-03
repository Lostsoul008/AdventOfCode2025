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


def get_invalid_arbitrary(ranges: List[tuple[int, int]]) -> List[int]:
	result: List[int] = []
	for start, end in ranges:
		for i in range(start, end + 1):
			str_i = str(i)
			length = len(str_i)
			mid = length // 2

			for sub_len in range(1, mid + 1):
				if length % sub_len != 0:
					continue

				sub_string = str_i[:sub_len]
				total = length // sub_len

				is_repeating = True
				for j in range(1, total):
					if sub_string != str_i[j * sub_len : (j+1) * sub_len]:
						is_repeating = False
						break

				if is_repeating:
					result.append(i)
					break

	return result


def main() -> None:
	file_input = getLines()
	print(f'{sum(get_invalid(get_ranges(file_input))) = }')
	print(f'{sum(get_invalid_arbitrary(get_ranges(file_input))) = }')


if __name__ == '__main__':
	main()
