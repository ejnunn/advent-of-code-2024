import argparse
from collections import defaultdict

def parse_input(filename):
    totals = []
    nums = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

        for line in lines:
            total, numbers = line.split(":")
            totals.append(int(total))
            nums.append(list(map(int, numbers.split())))
            
    return totals, nums

def pt2():
    return 0

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day7.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    totals, nums = parse_input(args.filename)

    part2_answer = pt2()

    print(f"Part 2: total = {part2_answer}")

