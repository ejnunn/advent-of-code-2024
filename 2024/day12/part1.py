from pprint import pprint
import argparse

def parse_input(filename):
    """
    Templated to read each line and put them in an array.
    """
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        
    return [list(line) for line in lines]

def identify_regions(grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    regions = []

    def flood_fill(r, c, plant_type):
        stack = [(r, c)]
        region = []
        while stack:
            x, y = stack.pop()
            if not (0 <= x < rows and 0 <= y < cols) or visited[x][y] or grid[x][y] != plant_type:
                continue
            visited[x][y] = True
            region.append((x, y))
            stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
        return region

    for r in range(rows):
        for c in range(cols):
            if not visited[r][c]:
                plant_type = grid[r][c]
                region = flood_fill(r, c, plant_type)
                if region:
                    regions.append(region)

    return regions

def calculate_perimeter(region, grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    for x, y in region:
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+dx, y+dy
            if not (0 <= nx < rows and 0 <= ny < cols) or grid[nx][ny] != grid[x][y]:
                perimeter += 1
    return perimeter


def pt1(grid):
    total_cost = 0

	# Identify all regions
    regions = identify_regions(grid)
    
    # Calculate perimeter for all reigons
    for region in regions:
        perimeter = calculate_perimeter(region, grid)
        area = len(region)
        total_cost += area * perimeter

    return total_cost

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day12.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    parsed_input = parse_input(args.filename)

    part1_answer = pt1(parsed_input)

    print(f"Part 1: total = {part1_answer}")

