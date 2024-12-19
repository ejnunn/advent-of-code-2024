def parse_input(filename):
	left = []
	right = []
	with open('input.txt', 'r') as file:
	    lines = file.read().splitlines()

	    for line in lines:
	    	first, second = map(int, line.split())
	    	left.append(first)
	    	right.append(second)
	return left, right

def main():
	# Parse input text file and split into left and right lists
	left, right = parse_input("input.txt")
	
	# Sort lists
	left = sorted(left)
	right = sorted(right)

	# Get difference between each pair of numbers and sum it all up
	total = 0
	for l, r in zip(left, right):
		total += abs(l - r)

	return total
	

if __name__ == '__main__':
	print(main())
