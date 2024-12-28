import argparse
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


def track_block_positions(block_ids):
    block_positions = defaultdict(list)
    for i, block in enumerate(block_ids):
        if block != ".":
            block_positions[block].append(i)
    return block_positions


def defrag_v2(block_ids):
    block_positions = track_block_positions(block_ids)
    new_block_ids = block_ids[:]
    free_space_spans = []
    free_start = None

    # Identify contiguous spans of free space
    for i, block in enumerate(new_block_ids):
        if block == ".":
            if free_start is None:
                free_start = i
        else:
            if free_start is not None:
                free_space_spans.append((free_start, i))
                free_start = None
    if free_start is not None:
        free_space_spans.append((free_start, len(new_block_ids)))

    print(f"free_space_spans = {free_space_spans}")

    # Move blocks in reverse order of IDs
    for block_id in sorted(block_positions.keys(), key=int, reverse=True):
        positions = block_positions[block_id]
        block_size = len(positions)

        for start, end in free_space_spans:
            if end - start >= block_size:
                # Place the block
                new_block_ids[start:start + block_size] = [block_id] * block_size
                # Clear old positions
                for pos in positions:
                    new_block_ids[pos] = "."
                # Update the free space span
                free_space_spans.remove((start, end))
                if start + block_size < end:
                    free_space_spans.append((start + block_size, end))
                free_space_spans.sort()
                break

    print(f"new_block_ids = {''.join(new_block_ids)}")

    return new_block_ids


def calculate_checksum(blocks):
    return sum(i * int(block) for i, block in enumerate(blocks) if block != ".")


def pt2(disk_map):
    block_ids = convert_disk_map_to_block_ids(disk_map)
    defragmented_blocks = defrag_v2(block_ids)
    return calculate_checksum(defragmented_blocks)


if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day9.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument
    disk_map = parse_input(args.filename)
    part2_answer = pt2(disk_map)
    print(f"Part 2 Answer: checksum = {part2_answer}")
