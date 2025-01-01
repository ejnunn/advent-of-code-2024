import argparse
import re
from collections import defaultdict

# Global Variables
SIMULATIONS = 100
WIDTH = 11
HEIGHT = 7
DEBUG = True


def parse_input(filename):
    with open(filename, 'r') as file:
        return [robot.strip("\n") for robot in file]

def extract_robot(robot):
	integers = list(map(int, re.findall(r'-?\d+', robot)))
	return integers

def simulate_robot(robot, WIDTH, HEIGHT):
	# Get robot position and velocity
	px, py, vx, vy = extract_robot(robot)

	# Simulate robot
	px += vx * SIMULATIONS
	py += vy * SIMULATIONS

	# Wrap robot back into bounds
	px %= WIDTH
	py %= HEIGHT

	# Handle negative bounds
	px = (px + WIDTH) % WIDTH
	py = (py + HEIGHT) % HEIGHT

	return px, py

def print_grid(robot_positions):
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            if x == WIDTH // 2 or y == HEIGHT // 2:
                row.append(' ')  # Grid lines
            elif (x, y) in robot_positions:
                row.append(str(robot_positions[(x, y)]))  # Robot count
            else:
                row.append('.')  # Empty space
        print(''.join(row))


def count_robots_in_quadrants(positions):
	TL, TR, BL, BR = 0, 0, 0, 0

	# Loop through each position
	# Determine which quadrant the robot is in
	# Ignore robots on the "grid-line" between each quadrant

	for position, count in positions.items():
		x, y = position[0], position[1]
		# Top-Left
		if x < WIDTH // 2 and y < HEIGHT // 2:
			TL += count

		# Top-Right
		elif x > WIDTH // 2 and y < HEIGHT // 2:
			TR += count

		# Bottom-Left
		elif x < WIDTH // 2 and y > HEIGHT // 2:
			BL += count

		# Bottom-Right
		elif x > WIDTH // 2 and y > HEIGHT // 2:
			BR += count

	return TL, TR, BL, BR


def pt1(robots):
	final_positions = defaultdict(int)

	# Run Simulation to get final positions of all robots
	for robot in robots:
		px, py = simulate_robot(robot, WIDTH, HEIGHT)
		
		final_positions[(px, py)] += 1
	
	if DEBUG:
		print_grid(final_positions)

	# Sum robots in each quadrant
	# Top-Left, Top-Right, Bottom-Left, Bottom-Right
	TL, TR, BL, BR = count_robots_in_quadrants(final_positions)

	if DEBUG:
		print(f"TL, TR, BL, BR = {TL}, {TR}, {BL}, {BR}")

	# Return "safety factory" (i.e. product of sums)
	safety_factor = (TL * TR * BL * BR)

	return safety_factor

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day14.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    robots = parse_input(args.filename)
    part1_answer = pt1(robots)
    print(f"Part 1 Answer: {part1_answer}")
