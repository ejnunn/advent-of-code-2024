import argparse
from collections import defaultdict

def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        
    return [[int(char) for char in line] for line in lines]

def find_trailheads(_map):
	return [(x, y) for y in range(len(_map)) for x in range(len(_map[0])) if _map[y][x] == 0]

def score(_map, trailhead):
	# Starting at the (x,y) trailhead, count how many peaks (9) can be reached
	# by only traversing neighbors that are +1 than current cell
	
	# DFS setup
	peaks = set()
	visited = set()
	visited.add(trailhead)

	def dfs(x, y):
		nonlocal peaks

		# Base Case
		if _map[y][x] == 9:
			peaks.add((x,y))

		for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			nx, ny = x+dx, y+dy

			# If next cell is in bounds, not visited, and increases by 1
			if 0 <= nx < len(_map[0]) and 0 <= ny < len(_map) and (nx, ny) not in visited and _map[ny][nx] == _map[y][x] + 1:
				visited.add((nx, ny))
				dfs(nx, ny)

	dfs(trailhead[0], trailhead[1])

	return len(peaks)

def pt1(_map):
	trailhead_scores = []

	# Find all trailheads
	trailheads = find_trailheads(topographic_map)
	print(trailheads)

	# Calculate score for each trailhead
	for trailhead in trailheads:
		trail_score = score(_map, trailhead)
		trailhead_scores.append(trail_score)

	return sum(trailhead_scores)

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day1.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    topographic_map = parse_input(args.filename)

    part1_answer = pt1(topographic_map)

    print(f"Part 1: total = {part1_answer}")
