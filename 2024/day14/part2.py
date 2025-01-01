import argparse
import os
import re
from collections import defaultdict
import time

# Global Variables
SIMULATIONS = 10000
WIDTH = 101
HEIGHT = 103
DEBUG = False


def parse_input(filename):
    with open(filename, 'r') as file:
        return [robot.strip("\n") for robot in file]

def extract_robot(robot):
	integers = list(map(int, re.findall(r'-?\d+', robot)))
	return integers

def simulate_robot(robot, WIDTH, HEIGHT, iteration):
	# Get robot position and velocity
	px, py, vx, vy = extract_robot(robot)

	# Simulate robot
	px += vx * iteration
	py += vy * iteration

	# Wrap robot back into bounds
	px %= WIDTH
	py %= HEIGHT

	# Handle negative bounds
	px = (px + WIDTH) % WIDTH
	py = (py + HEIGHT) % HEIGHT

	return px, py

def print_grid(robot_positions):
    grid = []
    for y in range(0, HEIGHT, 2):
        row = []
        for x in range(WIDTH):
            if (x, y) in robot_positions and (x,y+1) in robot_positions:
                row.append(":")
            elif (x,y) in robot_positions:
            	row.append("'")
            elif (x,y+1) in robot_positions:
            	row.append(".")
            else:
                row.append(' ')  # Empty space
        grid.append(''.join(row))

    return grid


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


def pt2(robots, starting_iteration):
	min_frame = -1
	min_safety_factory = float('inf')

	# Run Simulation to get final positions of all robots
	for i in range(starting_iteration, SIMULATIONS):
		final_positions = defaultdict(int)

		# Simulate one second
		for robot in robots:
			px, py = simulate_robot(robot, WIDTH, HEIGHT, i)
			
			final_positions[(px, py)] += 1
		
		# Horizontal stripes appear every 103 frames, starting at frame 33.
		# This only prints frames that contain horizontal stripes
		# The tree appears at frame 7861
		if (i - starting_iteration) % 103 == 0:
			time.sleep(0.3)
			print("\033[H")
			grid = print_grid(final_positions)
			print(f"iteration: {i}")
			print("\n".join(grid), end="", flush=True)

		
		# Sum robots in each quadrant
		# Top-Left, Top-Right, Bottom-Left, Bottom-Right
		TL, TR, BL, BR = count_robots_in_quadrants(final_positions)

	# Return "safety factory" (i.e. product of sums)
	safety_factor = (TL * TR * BL * BR)

	if safety_factor < min_safety_factory:
		min_safety_factory = safety_factor
		min_frame = i

	return min_frame

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day14.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    parser.add_argument('starting_iteration', type=int, help="The starting iteration of the simulation.")
    args = parser.parse_args()

    # Use the filename argument
    robots = parse_input(args.filename)
    part2_answer = pt2(robots, args.starting_iteration)
    print(f"Part 2 Answer: {part2_answer}")
