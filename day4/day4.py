import argparse

def parse_input(filename):
	with open(filename, 'r') as file:
		return file.read().splitlines()

def pt1(word_search):
	word = "XMAS"
	word_len = len(word)
	count = 0
	rows = len(word_search)
	cols = len(word_search[0])

	directions = [
		(0, 1),  # Right
		(1, 0),  # Down
		(1, 1),  # Down-right diagonal
		(1, -1), # Down-left diagonal
		(0, -1), # Left (reverse of right)
		(-1, 0), # Up (reverse of down)
		(-1, -1),# Up-left diagonal (reverse of down-left)
		(-1, 1)  # Up-right diagonal (reverse of down-right)
	]

	# Helper function to check if the word "XMAS" exists in the given direction
	def check_direction(row, col, row_delta, col_delta):
		# Iterate over each character in the word "XMAS"
		for i in range(word_len):
			# Calculate the next row and column to check based on the direction
			next_row = row + row_delta * i
			next_col = col + col_delta * i

			# Check if the next position is out of bounds or if the character doesn't match the word
			if next_row < 0 or next_row >= rows or next_col < 0 or next_col >= cols:
				# If out of bounds, return False
				return False
			if word_search[next_row][next_col] != word[i]:
				# If the character doesn't match, return False
				return False

		# If all characters match in the direction, return True
		return True

	for r in range(rows):
		for c in range(cols):
			# Check if we can fit the word in any direction
			for dr, dc in directions:
				if check_direction(r, c, dr, dc):
					count += 1

	return count

def pt2(word_search):
	count = 0
	rows = len(word_search)
	cols = len(word_search)

	def is_cross(row, col):
		"""
		M.S        M.S
		.A.   or   .A.
		M.S        S.M

		"""
		if word_search[row][col] != "A":
			return False

		try:
			# First diagonal (top-left to bottom-right)
			top_left = word_search[row-1][col-1]
			bottom_right = word_search[row+1][col+1]

			# Second diagonal (top-right to bottom-left)
			top_right = word_search[row-1][col+1]
			bottom_left = word_search[row+1][col-1]

			first_diagonal = (top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M")
			second_diagonal = (top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M")

			return first_diagonal and second_diagonal

		except IndexError:
			return False


	for r in range(rows):
		for c in range(cols):
			if is_cross(r, c):
				count += 1

	return count


if __name__ == '__main__':
    # Argument parsing to get the input file name
    parser = argparse.ArgumentParser(description="Process the word search.")
    parser.add_argument('filename', type=str, help="The path to the word search input file.")
    args = parser.parse_args()

    # Parse the input file into corrupted memory lines
    word_search = parse_input(args.filename)

    # Calculate results for Part 1 and Part 2
    part1_answer = pt1(word_search)
    part2_answer = pt2(word_search)

    # Output the results
    print(f"Part 1: total = {part1_answer}")
    print(f"Part 2: total = {part2_answer}")
