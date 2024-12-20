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

def pt2(left, right):
    # Get frequency of numbers in right list
    right_freq = defaultdict(int)
    for r in right:
        right_freq[r] += 1

    # Get total similarity score by adding up each number in the left list after multiplying it
    # by the number of times the right number occurs.
    total = 0
    for num in left:
        total += num * right_freq[num]
    return total

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day1.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    left, right = parse_input(args.filename)

    part2_answer = pt2(left, right)

    print(f"Part 2: total = {part2_answer}")
