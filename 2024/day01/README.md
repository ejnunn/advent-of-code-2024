# Advent of Code 2024 - Day 1: Historian Hysteria

This directory contains my Python solutions for Day 1 of the [Advent of Code 2024](https://adventofcode.com/2024/day/1) challenge.

## Puzzle Description

The Chief Historian is missing, and a group of Senior Historians needs to compile a list of historically significant location IDs to find him. They have two lists of location IDs, but the lists differ. To reconcile them, they decide to pair the smallest numbers from each list, the second smallest, and so on, calculating the absolute difference for each pair. The task is to compute the total of these differences.

## Solution Approach

1. **Input Parsing**: Read the two lists of integers from the provided input file.
2. **Sorting**: Sort both lists in ascending order.
3. **Pairing and Calculation**: Pair corresponding elements from both lists and compute the absolute difference for each pair.
4. **Summation**: Sum all the absolute differences to get the total distance.

## Files

- `example_input.txt`: Contains the example input from the problem statement.
    Contains the puzzle input with two columns of location IDs.
- `real_input.txt`: Contains the puzzle input with two columns of location IDs.
- `part1.py`: Python script implementing the solution for Part 1 of the puzzle.
- `part2.py`: Python script implementing the solution for Part 2 of the puzzle. 
- `README.md`: This file, providing an overview of the puzzle and solution.

## Usage

1. Ensure you have Python 3 installed.
2. Place your puzzle input into `real_input.txt`.
3. Run the solution script:
   ```bash
   python part1.py real_input.txt

