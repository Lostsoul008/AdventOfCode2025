import os
import pathlib
import re
from contextlib import contextmanager
from typing import List, Any, Generator

type Lines = List[str]


@contextmanager
def change_working_directory() -> Generator[None, Any, None]:
	cwd = pathlib.Path.cwd()
	os.chdir(os.path.dirname(__file__))
	try:
		yield
	finally:
		os.chdir(cwd)


def get_lines(day: int, _file: str = None) -> List[str]:
	with change_working_directory():
		if _file is None:
			_file = 'input.txt'
		path = pathlib.Path('../Data') / f'Day{day}/' / _file
		print(f'Using input file {path}')
		try:
			return list(path.read_text().strip('\n').split('\n'))
		except FileNotFoundError:
			print(f'File "{_file}" not found.')
			return []


def get_numbers_all(_lines: Lines) -> list[list[int]]:
	result: List[List[int]] = []
	for line in _lines:
		l1 = []
		if line:
			nums = re.split(r'\D+', line)
			for num in nums:
				l1.append(int(num))
		result.append(l1)

	return result


def get_numbers_fl(_lines: Lines) -> tuple[list[int], list[int]]:
	l1 = []
	l2 = []
	for line in _lines:
		nums = re.split(r'\D+', line)
		l1.append(int(nums[0]))
		l2.append(int(nums[-1]))

	return l1, l2
