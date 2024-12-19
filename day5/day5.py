import argparse

def parse_input(filename):
	with open(filename, 'r') as file:
		sections = file.read().strip().split("\n\n")
		rules = []
		for line in sections[0].splitlines():
			x, y = map(int, line.split('|'))
			rules.append((x, y))
		updates = [list(map(int, line.split(','))) for line in sections[1].splitlines()]
	return rules, updates

def is_update_valid(update, rules):
	update_positions = {page: i for i, page in enumerate(update)}
	for x, y in rules:
		if x in update_positions and y in update_positions:
			if update_positions[x] > update_positions[y]:
				return False
	return True

def order_update(update, rules):
    # Build a dependency graph
    from collections import defaultdict, deque

    # Graph and in-degree tracking
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    # Only consider rules where both X and Y are in the update
    update_set = set(update)
    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            if x not in in_degree:
                in_degree[x] = 0

    # Perform topological sort
    # Initialize queue with nodes that have no incoming edges
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_pages = []

    while queue:
        node = queue.popleft()
        sorted_pages.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If the sorted pages cover all the pages in the update, return them
    if len(sorted_pages) == len(update):
        return sorted_pages
    else:
        raise ValueError("Circular dependency detected or incomplete graph.")


def pt1(rules, updates):
	total = 0
	for update in updates:
		if is_update_valid(update, rules):
			middle_page = len(update) // 2
			total += update[middle_page]
	return total

def pt2(rules, updates):
	total = 0

	for update in updates:
		if not is_update_valid(update, rules):
			ordered_update = order_update(update, rules)
			middle_page = len(ordered_update) // 2
			total += ordered_update[middle_page]

	return total


if __name__ == '__main__':
    # Argument parsing to get the input file name
    parser = argparse.ArgumentParser(description="Process the word search.")
    parser.add_argument('filename', type=str, help="The path to the word search input file.")
    args = parser.parse_args()

    # Parse the input file into corrupted memory lines
    rules, updates = parse_input(args.filename)

    # Calculate results for Part 1 and Part 2
    part1_answer = pt1(rules, updates)
    part2_answer = pt2(rules, updates)

    # Output the results
    print(f"Part 1: total = {part1_answer}")
    print(f"Part 2: total = {part2_answer}")


   