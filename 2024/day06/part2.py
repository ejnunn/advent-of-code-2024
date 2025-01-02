from pprint import pprint
import argparse
import copy

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
    while is_valid_position(matrix, guard_i, guard_j) and (guard_i, guard_j, direction) not in visited:
        # Visit current square
        visited.add((guard_i, guard_j, direction))

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

def pt2(matrix):
    """
    Identify positions where adding an obstruction traps the guard in a loop.
    """
    possible_positions = set()
    start_i, start_j = get_start_position(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Skip non-empty cells and the guard's starting position
            if matrix[i][j] != "." or (i, j) == (start_i, start_j):
                continue

            # Test the effect of placing an obstruction
            test_matrix = copy.deepcopy(matrix)
            test_matrix[i][j] = "O"

            print(f"Placing O at ({i},{j})")

            _, is_loop = simulate_guard(test_matrix)
            if is_loop:
                possible_positions.add((i, j))

    return len(possible_positions)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Advent of Code Day 6 Part 2.")
    parser.add_argument('filename', type=str, help="Input file containing the grid.")
    args = parser.parse_args()

    # Parse the input file
    matrix = parse_input(args.filename)

    # Calculate the answer for Part 2
    part2_answer = pt2(matrix)
    print(f"Part 2: total = {part2_answer}")
