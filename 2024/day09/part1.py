import argparse
from pprint import pprint
from collections import defaultdict

def parse_input(filename):
    with open(filename, 'r') as file:
        return file.read().strip() 

def convert_disk_map_to_block_ids(disk_map):
	block_ids = []

	curr_id = 0
	for i, digit in enumerate(disk_map):
		if i % 2 == 0:
			block_ids.extend([str(curr_id)] * int(digit))
			curr_id += 1
		else:
			block_ids.extend(["."] * int(digit))

	return block_ids

def defrag(block_ids):

    # Initialize pointers
    left = 0
    right = len(block_ids) - 1

    # Move all dots to the right of the digits
    while left < right:
        # Find the next dot on the left
        while left < right and block_ids[left] != ".":
            left += 1

        # Find the next digit on the right
        while left < right and block_ids[right] == ".":
            right -= 1

        # Swap if valid
        if left < right:
            block_ids[left], block_ids[right] = block_ids[right], block_ids[left]
            left += 1
            right -= 1

    return block_ids


def calculate_checksum(blocks):
	checksum = 0

	for i, block in enumerate(blocks):
		if "." == block:
			break
		checksum += i * int(block)

	return checksum


def pt1(disk_map):
	print(f"disk_map = {disk_map}")

	block_ids = convert_disk_map_to_block_ids(disk_map)
	print(f"block_ids = {block_ids}")

	defragmented_blocks = defrag(block_ids)
	print(f"defragmented_blocks = {defragmented_blocks}")

	checksum = calculate_checksum(defragmented_blocks)
	print(f"checksum = {checksum}")

	return checksum


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day9.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    disk_map = parse_input(args.filename)

    part1_answer = pt1(disk_map)

    print(f"Part 1: total = {part1_answer}")
