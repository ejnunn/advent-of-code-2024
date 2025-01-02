import argparse
from collections import defaultdict
from itertools import product

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

def generate_operator_combinations(n):
    """
    Generate all possible combinations of * and + for n positions.
    :param n: Number of positions (length of each combination).
    :return: List of lists containing all combinations of * and +.
    """
    operators = ["*", "+", "||"]
    combinations = list(product(operators, repeat=n))
    return [list(comb) for comb in combinations]


def equation_possibly_true(target, values):
    operator_combinations = generate_operator_combinations(len(values)-1)

    for combination in operator_combinations:
        curr_total = values[0]
        for i in range(len(combination)):
            if combination[i] == "*":
                curr_total *= values[i+1]
            elif combination[i] == "||":
                curr_total = int(str(curr_total) + str(values[i+1]))
            else:
                curr_total += values[i+1]
            # Make sure to only consider a valid solution if all values have been used.
            # E.g. target:10, values:[3,2,4,1], invalid = 3*2+4 = 10 (1 not used)...valid = 3*2+4*1 = 10
            if i == len(combination)-1 and curr_total == target:
                expression = "".join(str(value) + op for value, op in zip(values, combination)) + str(values[-1])
                print(f"Found a solution: {target} = {expression}")
                return True

    return False

def pt1(totals, nums):
    answer = 0

    for total, values in zip(totals, nums):
        if equation_possibly_true(total, values):
            answer += total

    return answer

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day7.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    totals, nums = parse_input(args.filename)

    part1_answer = pt1(totals, nums)

    print(f"Part 1: total = {part1_answer}")
