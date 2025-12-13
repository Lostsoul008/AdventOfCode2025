import math
from copy import deepcopy
from typing import Optional

from file_helpers import Lines, get_lines


def calc_dist(start: list[int], end: list[int]) -> float:
	return math.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2 + (start[2] - end[2])**2)


def part_1(lines: Lines, connections: int) -> int:
	boxes: list[list[int]] = [[]] * len(lines)

	for i, line in enumerate(lines):
		boxes[i] = ([int(a) for a in line.split(',')])

	distances: list[tuple[float, int, int]] = []

	for i, box1 in enumerate(boxes):
		for j, box2 in enumerate(boxes):
			if i != j:
				distances.append((calc_dist(box1, box2), i, j))

	distances.sort(key=lambda x: x[0], reverse=True)

	pairs: set[tuple[int, int]] = set()
	circuits: list[list[int]] = []
	circuit_lookup: dict[int, int] = {}

	for con in range(connections):
		while True:
			_, temp_box1, temp_box2 = distances.pop()
			if (temp_box1, temp_box2) not in pairs:
				break

		pairs.add((temp_box1, temp_box2))
		pairs.add((temp_box2, temp_box1))

		box1_circuit: int = circuit_lookup.get(temp_box1, -1)
		box2_circuit: int = circuit_lookup.get(temp_box2, -1)

		if box1_circuit == -1 and box2_circuit == -1:
			circuit_lookup[temp_box1] = len(circuits)
			circuit_lookup[temp_box2] = len(circuits)
			circuits.append([temp_box1, temp_box2])

		elif box1_circuit == -1:
			circuit_lookup[temp_box1] = box2_circuit
			circuits[box2_circuit].append(temp_box1)

		elif box2_circuit == -1:
			circuit_lookup[temp_box2] = box1_circuit
			circuits[box1_circuit].append(temp_box2)
		elif box1_circuit != box2_circuit:
			old_circuit = circuits[box2_circuit]

			for x in old_circuit:
				circuit_lookup[x] = box1_circuit
			circuits[box1_circuit].extend(old_circuit)
			circuits[box2_circuit] = []

	for i in range(len(boxes)):
		if i not in circuit_lookup:
			circuits.append([i])

	results = sorted([len(x) for x in circuits], reverse=True)

	return results[0] * results[1] * results[2]


def main() -> None:
	# file_input = get_lines(8, 'example_input.txt')
	# print(f'Part 1 = {part_1(file_input, 10)}')
	file_input = get_lines(8)
	print(f'Part 1 = {part_1(file_input, 1000)}')

if __name__ == '__main__':
	main()
