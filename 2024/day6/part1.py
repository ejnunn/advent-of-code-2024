from pprint import pprint
import argparse

def parse_input(filename):
    matrix = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        for line in lines:
            matrix.append(list(line))
    return matrix

def get_start_position(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "^":
                return i, j

def is_valid_position(matrix, i, j):
    return 0 <= i < len(matrix) and 0 <= j < len(matrix[0])


def simulate_guard(matrix):
    matrix_len = len(matrix)
    matrix_width = len(matrix[0])
    # Direction is mapped from guard symbol to (i,j) pairs
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # Game loop. Continue until guard has left the matrix
    visited = set()
    guard_i, guard_j = get_start_position(matrix)
    direction = 0
    while is_valid_position(matrix, guard_i, guard_j):
        # Visit current square
        visited.add((guard_i, guard_j))

        # If facing a wall, turn right
        next_i = guard_i + directions[direction][0]
        next_j = guard_j + directions[direction][1]
        if is_valid_position(matrix, next_i, next_j) and matrix[next_i][next_j] in ["#", "O"]:
             direction = (direction + 1) % 4

        # Else move one step forward
        guard_i += directions[direction][0]
        guard_j += directions[direction][1]

        # Check if guard leaves the matrix
        if not is_valid_position(matrix, guard_i, guard_j):
            return visited, False

    return visited, True

def pt1(matrix):
    visited, _ = simulate_guard(matrix)

    return len(visited)

if __name__ == '__main__':
    # Argument parsing to get the input file name
    parser = argparse.ArgumentParser(description="Process the word search.")
    parser.add_argument('filename', type=str, help="The path to the word search input file.")
    args = parser.parse_args()

    # Parse the input file into corrupted memory lines
    matrix = parse_input(args.filename)

    # Part 1
    part1_answer = pt1(matrix)
    print(f"Part 1: total = {part1_answer}")
