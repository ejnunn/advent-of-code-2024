import argparse

def parse_input(filename):
	"""
	Templated to read each line and put them in an array.
	"""
    with open(filename, 'r') as file:
        lines = file.read().splitlines()
        
    return lines

def pt1():
	pass

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day1.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    parsed_input = parse_input(args.filename)

    part1_answer = pt1(parsed_input)

    print(f"Part 1: total = {part1_answer}")

