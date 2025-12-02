import re
import sys
from typing import IO, List, Optional

type Lines = List[str]

def getFile(options: str, _file: str = None) -> IO[str]:
	if _file:
		return open(_file, options)

	return open('input.txt', options)


def getLines(_file: str = None) -> List[str]:
	with getFile('r', _file) as f:
		return [x.rstrip('\n') for x in f.readlines()]


def getnumbersall(_lines: Lines) -> list[list[int]]:
	result: List[List[int]] = []
	for line in _lines:
		l1 = []
		if line:
			nums = re.split(r'\D+', line)
			for num in nums:
				l1.append(int(num))
		result.append(l1)

	return result


def getnumbersfl(_lines: Lines) -> tuple[list[int], list[int]]:
	l1 = []
	l2 = []
	for line in _lines:
		nums = re.split(r'\D+', line)
		l1.append(int(nums[0]))
		l2.append(int(nums[-1]))

	return l1, l2
