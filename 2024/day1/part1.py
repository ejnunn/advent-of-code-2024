import argparse
from collections import defaultdict

def parse_input(filename):
    left = []
    right = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

        for line in lines:
            first, second = map(int, line.split())
            left.append(first)
            right.append(second)
    return left, right

def pt1(left, right):
    # Sort lists
    left = sorted(left)
    right = sorted(right)

    # Get difference between each pair of numbers and sum it all up
    total = 0
    for l, r in zip(left, right):
        total += abs(l - r)

    return total

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day1.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    left, right = parse_input(args.filename)

    part1_answer = pt1(left, right)

    print(f"Part 1: total = {part1_answer}")
