import argparse
import re

# Function to parse input from the file
def parse_input(filename):
    corrupted_memory = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        corrupted_memory = lines  # Store all lines for processing
    return corrupted_memory

# Function for Part 1: Basic multiplication handling
def pt1(corrupted_memory):
    total = 0
    # Loop through each line and calculate the total
    for line in corrupted_memory:
        # Find all mul instructions and sum their results
        for match in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line):
            num1, num2 = int(match[0]), int(match[1])
            total += num1 * num2
    return total

# Function for Part 2: Handle do() and don't() to enable/disable multiplications
def pt2(corrupted_memory):
    total = 0
    mul_enabled = True  # mul is enabled initially

    # Loop through each line of corrupted memory
    for line in corrupted_memory:
        split_parts = re.split(r'(do\(\)|don\'t\(\))', line)

        # Process the mul() instructions if enabled
        for part in split_parts:
        	if part == "do()":
        		mul_enabled = True
        	elif part == "don't()":
        		mul_enabled = False
        	else:
	        	if mul_enabled:
	        		for match in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", part):
	        			num1, num2 = int(match[0]), int(match[1])
	        			total += num1 * num2
    
    return total

if __name__ == '__main__':
    # Argument parsing to get the input file name
    parser = argparse.ArgumentParser(description="Process the corrupted memory.")
    parser.add_argument('filename', type=str, help="The path to the corrupted memory input file.")
    args = parser.parse_args()

    # Parse the input file into corrupted memory lines
    corrupted_memory = parse_input(args.filename)

    # Calculate results for Part 1 and Part 2
    part1_answer = pt1(corrupted_memory)
    part2_answer = pt2(corrupted_memory)

    # Output the results
    print(f"Part 1: total = {part1_answer}")
    print(f"Part 2: total = {part2_answer}")
