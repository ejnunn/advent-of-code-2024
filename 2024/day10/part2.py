import argparse
from collections import defaultdict

def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
    return [[int(char) for char in line] for line in lines]

def find_trailheads(_map):
    return [(x, y) for y in range(len(_map)) for x in range(len(_map[0])) if _map[y][x] == 0]

def rating(_map, trailhead):
    # Starting at the (x, y) trailhead, count how many unique paths reach a peak (9)
    visited = set()
    visited.add(trailhead)
    total_paths = 0

    def dfs(x, y):
        nonlocal total_paths

        # If this is a peak, increment the path count
        if _map[y][x] == 9:
            total_paths += 1
            return

        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # If the next cell is in bounds, not visited, and increases by 1
            if (
                0 <= nx < len(_map[0]) and
                0 <= ny < len(_map) and
                (nx, ny) not in visited and
                _map[ny][nx] == _map[y][x] + 1
            ):
                visited.add((nx, ny))
                dfs(nx, ny)
                visited.remove((nx, ny))  # Backtrack

    dfs(trailhead[0], trailhead[1])
    return total_paths

def pt2(_map):
    trailhead_ratings = []

    # Find all trailheads
    trailheads = find_trailheads(_map)

    # Calculate score for each trailhead
    for trailhead in trailheads:
        trail_rating = rating(_map, trailhead)
        trailhead_ratings.append(trail_rating)

    return sum(trailhead_ratings)

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day10.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    topographic_map = parse_input(args.filename)

    part2_answer = pt2(topographic_map)

    print(f"Part 2: total = {part2_answer}")
