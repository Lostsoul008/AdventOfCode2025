import math
from typing import Optional

from file_helpers import Lines, get_lines


def calc_dist(start: list[int], end: list[int]) -> float:
	return math.sqrt((start[0] - end[0])**2 + (start[1] - end[1])**2 + (start[2] - end[2])**2)


def part_1(lines: Lines, until_complete: bool, connections: int = 0) -> int:
	boxes: list[list[int]] = [[]] * len(lines)
	distances: list[tuple[float, int, int]] = []
	pairs: set[tuple[int, int]] = set()
	circuits: list[list[int]] = []
	circuit_lookup: dict[int, Optional[int]] = {}
	temp_box1, temp_box2 = -1, -1

	# Initialize Junction Box Data
	for i, line in enumerate(lines):
		boxes[i] = ([int(a) for a in line.split(',')])

	#Find All Distances and Sort
	for i, box1 in enumerate(boxes):
		for j, box2 in enumerate(boxes):
			if i != j:
				distances.append((calc_dist(box1, box2), i, j))

	distances.sort(key=lambda x: x[0], reverse=True)

	#Initialize circuit data structures
	for i in range(len(boxes)):
		circuit_lookup[i] = None
		circuits.append([i])

	# Loop until the end of connections or Infinite if part 2
	con = 0
	while con < connections or until_complete:
		con += 1

		# Break for Part 2
		if len([c for c in circuits if c != []]) == 1:
			# print("found one circuit ", con)
			break

		#Find next valid pair
		while True:
			_, temp_box1, temp_box2 = distances.pop()
			if (temp_box1, temp_box2) not in pairs:
				break

		pairs.add((temp_box1, temp_box2))
		pairs.add((temp_box2, temp_box1))

		#Check if the boxes to connect are already on a circuit
		#Merge Data Circuit Data Structure
		#Update Lookup to new Circuit index
		box1_circuit: Optional[int] = circuit_lookup.get(temp_box1, None)
		box2_circuit: Optional[int] = circuit_lookup.get(temp_box2, None)

		if box1_circuit is not None and box1_circuit == box2_circuit:
			continue

		if box1_circuit is None and box2_circuit is None:
			circuit_lookup[temp_box1] = temp_box1
			circuit_lookup[temp_box2] = temp_box1
			circuits[temp_box1].append(temp_box2)
			circuits[temp_box2] = []

		elif box2_circuit is None:
			circuit_lookup[temp_box2] = box1_circuit
			circuits[box1_circuit].append(temp_box2)
			circuits[temp_box2] = []

		elif box1_circuit is None:
			circuit_lookup[temp_box1] = box2_circuit
			circuits[box2_circuit].append(temp_box1)
			circuits[temp_box1] = []
		else:
			old_circuit = circuits[box2_circuit]

			for x in old_circuit:
				circuit_lookup[x] = box1_circuit
			circuits[box1_circuit].extend(old_circuit)
			circuits[box2_circuit] = []

	# If Part 1 multiply the largest 3
	if not until_complete:
		results = sorted([len(x) for x in circuits], reverse=True)

		return results[0] * results[1] * results[2]
	# If Part 2 multiply the last connection that was made in order to create one complete circuit
	else:
		return boxes[temp_box1][0] * boxes[temp_box2][0]


def main() -> None:
	# file_input = get_lines(8, 'example_input.txt')
	# print(f'Part 1 = {part_1(file_input, False, 10)}')
	# print(f'Part 2 = {part_1(file_input, True)}')
	file_input = get_lines(8)
	print(f'Part 1 = {part_1(file_input, False, 1000)}')
	print(f'Part 2 = {part_1(file_input, True)}')

if __name__ == '__main__':
	main()
