import argparse

def parse_input(filename):
    matrix = []
    with open(filename, 'r') as file:
        lines = file.read().splitlines()

        for line in lines:
            matrix.append([int(x) for x in line.split()])

    return matrix

def pt2(matrix):
    """
    Determine how many reports are safe, allowing the removal of one level.
    A report is safe if, after removing at most one level, it is strictly increasing or decreasing, 
    with each step within 1-3.
    """
    total = 0
    for report in matrix:
        if is_safe(report, removal_allowed=True):
            total += 1
    return total

def is_safe(report, removal_allowed):
    """
    Check if a report is safe.
    A report is safe if it is strictly increasing or decreasing with steps within 1-3.
    You can optionally remove one level to make the report safe.
    """
    def check_increasing(report):
        for i in range(1, len(report)):
            diff = report[i] - report[i-1]
            if diff <= 0 or abs(diff) > 3:
                return False
        return True

    def check_decreasing(report):
        for i in range(1, len(report)):
            diff = report[i-1] - report[i]
            if diff <= 0 or abs(diff) > 3:
                return False
        return True
    
    # First check if it's already increasing or decreasing
    if check_increasing(report) or check_decreasing(report):
        return True
    
    # If removal is allowed, try removing one level and check again
    if removal_allowed:
        for i in range(len(report)):
            # Try removing the current level and check if the report becomes safe
            modified_report = report[:i] + report[i+1:]
            if check_increasing(modified_report) or check_decreasing(modified_report):
                return True
    
    # If no condition holds, return False
    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Process an input file for day2.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Parse input to create report matrix
    matrix = parse_input(args.filename)

    part2_answer = pt2(matrix)

    print(f"Part 2: total = {part2_answer}")
