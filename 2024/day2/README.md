# Advent of Code 2024 - Day 2: Red-Nosed Reports

This directory contains my Python solutions for Day 2 of the [Advent of Code 2024](https://adventofcode.com/2024/day/2) challenge.

## Puzzle Description

The engineers at the Red-Nosed Reindeer nuclear fusion/fission plant need help analyzing unusual data from the reactor. Each report is a list of levels, and the goal is to determine which reports are safe based on specific rules:

1. The levels are either all increasing or all decreasing.
2. Any two adjacent levels differ by at least one and at most three.

### Part Two

The Problem Dampener module allows the reactor safety systems to tolerate a single bad level in what would otherwise be a safe report. The task is updated to count reports as safe if removing one level makes the report safe.

## Solution Approach

### Part 1
1. **Input Parsing**: Read the reports from the input file.
2. **Validation**: For each report, check if the levels are strictly increasing or decreasing, with adjacent differences between 1 and 3.
3. **Count Safe Reports**: Increment the count for reports that meet the safety criteria.

### Part 2
1. **Handle Problem Dampener**: Extend the logic to check if removing any single level from a report results in a valid safe report.
2. **Recount Safe Reports**: Include reports made safe by the Problem Dampener.

## Files

- `example_input.txt`: Example input provided in the problem statement.
- `real_input.txt`: Actual puzzle input for the challenge.
- `part1.py`: Python script implementing the solution for Part 1 of the puzzle.
- `part2.py`: Python script implementing the solution for Part 2 of the puzzle.
- `README.md`: This file, providing an overview of the puzzle and solution.

## Usage

1. Ensure you have Python 3 installed.
2. Place your puzzle input into `real_input.txt`.
3. Run the solution scripts:
   ```bash
   python part1.py real_input.txt
   python part2.py real_input.txt
   ```

