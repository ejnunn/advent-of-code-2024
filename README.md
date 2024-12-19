# Advent of Code 2024

This repository contains solutions for the **Advent of Code 2024** puzzles, implemented in Python. Advent of Code is an annual coding challenge event that provides a new puzzle every day from December 1st to December 25th.

## Table of Contents

- [About](#about)
- [Structure](#structure)
- [Requirements](#requirements)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## About

Advent of Code is a series of daily programming challenges that test problem-solving and algorithmic skills. Each day presents two parts of a puzzle, often requiring innovative and efficient solutions. Learn more about Advent of Code [here](https://adventofcode.com/).

This repository serves as my attempt to solve all 2024 puzzles using Python. Each solution is tailored to the specific problem but aims to prioritize clarity and efficiency.

## Structure

The repository is organized as follows:

```
.
├── day01
│   ├── input.txt       # Input data for Day 1
│   ├── part1.py        # Solution for Day 1, Part 1
│   ├── part2.py        # Solution for Day 1, Part 2
│   └── README.md       # Description of the Day 1 challenge
├── day02
│   ├── input.txt       # Input data for Day 2
│   ├── part1.py        # Solution for Day 2, Part 1
│   ├── part2.py        # Solution for Day 2, Part 2
│   └── README.md       # Description of the Day 2 challenge
...
└── README.md           # Project overview
```

Each `dayXX` folder contains:
- `input.txt`: Puzzle input for the day.
- `part1.py`: Solution for the first part of the puzzle.
- `part2.py`: Solution for the second part of the puzzle.
- `README.md`: Description of the puzzle and notes on the solution.

## Requirements

Ensure you have Python 3.8 or higher installed. You can manage dependencies using `pip`.

To install necessary packages:

```bash
pip install -r requirements.txt
```

(If applicable, a `requirements.txt` file should be included for any libraries used.)

## Usage

1. Navigate to the folder for the desired day.
2. Run the Python scripts:

   ```bash
   python part1.py
   python part2.py
   ```
3. Replace the contents of `input.txt` with your personal puzzle input from the Advent of Code website.

## Contributing

Feel free to fork this repository, solve the puzzles, and submit a pull request with your solutions or optimizations. Collaboration is encouraged, but please avoid posting solutions publicly before the puzzles are unlocked each day.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

