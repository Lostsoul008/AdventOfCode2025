from copy import copy
from dataclasses import dataclass

from file_helpers import Lines, get_lines

@dataclass
class Machine:
	lights: list[int]
	buttons: list[list[int]]
	joltages: list[int]


def parse_input(lines: Lines) -> list[Machine]:
	machines = []

	for line in lines:
		lights = []

		last_bracket = line.rindex(']')
		last_paren = line.rindex(')')

		for char in line[1:last_bracket]:
			if char == '#':
				lights.append(1)
			else:
				lights.append(0)

		buttons = []

		for button_str in line[last_bracket + 3:last_paren].split(') ('):
			buttons.append([int(char) for char in button_str.split(',')])

		joltages = [int(char) for char in line[last_paren + 3:-1].split(',')]

		machines.append(Machine(lights, buttons, joltages))
	return machines


def calculate_presses(machine: Machine) -> int:
	print(machine)

	def calculate_presses_rec(state: list[int], pressed: list[int]) -> int:
		to_fix: int = 0

		if state == machine.lights:
			return 0

		for i, light in enumerate(machine.lights):
			if state[i] != light:
				to_fix = i
				break

		minimum_presses = len(machine.buttons)

		for i, button in enumerate(machine.buttons):
			if i in pressed:
				continue

			if to_fix in button:
				new_state = copy(state)
				for light in button:
					new_state[light] ^= 1

				minimum_presses = min(minimum_presses, calculate_presses_rec(new_state, pressed + [i]))

		return minimum_presses + 1
	return calculate_presses_rec([0] * len(machine.lights), [])


def caclulate_all_presses(machines: list[Machine]) -> int:
	return sum([calculate_presses(m) for m in machines])


def main() -> None:
	# file_input = get_lines(10, 'example_input.txt')
	file_input = get_lines(10)

	machine_list = parse_input(file_input)
	print(f'Part 1 = {caclulate_all_presses(machine_list)}')

if __name__ == '__main__':
	main()
