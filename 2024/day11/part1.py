import argparse

def parse_input(filename):
    """
    Templated to read each line and put them in an array.
    """
    with open(filename, 'r') as file:
        single_line = file.read().splitlines()[0]
        stones = single_line.split(" ")
    
    return list(map(int, stones))

class Stone:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, input_array=None):
        self.head = None
        self.tail = None

        if input_array:
            self.build_from_array(input_array)

    def build_from_array(self, input_array):
        """
        Builds the linked list from a string of integers separated by spaces.
        """
        for val in input_array:
            self.append(val)

    def append(self, val):
        new_stone = Stone(val)
        if not self.head:  # If the list is empty
            self.head = new_stone
            self.tail = new_stone
        else:
            self.tail.next = new_stone
            new_stone.prev = self.tail
            self.tail = new_stone

    def split_stone(self, stone):
        # Create two new stones by splitting initial stone's value in half (literally)
        str_value = str(stone.val)
        mid = len(str_value) // 2
        left_val, right_val = str_value[:mid], str_value[mid:]
        left, right = Stone(int(left_val)), Stone(int(right_val))

        # Pointers for new stones
        left.prev = stone.prev
        left.next = right
        right.prev = left
        right.next = stone.next


        # Insert new stones to linked list
        if stone.prev:
            stone.prev.next = left
        else:
            self.head = left
        if stone.next:
            stone.next.prev = right
        else:
            self.tail = right

        del stone

    def blink(self):
        # For stone in linked list:
        # update each one
        curr = self.head
        while curr:
            if curr.val == 0:
                curr.val = 1
                curr = curr.next
            elif len(str(curr.val)) % 2 == 0:
                # Even digits get split into two stones.
                # Left stone has left-half of digits and vice versa
                next_stone = curr.next
                self.split_stone(curr)
                curr = next_stone
            else:
                # Default is to multiply by 2024
                curr.val *= 2024
                curr = curr.next

    def count_stones(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def display(self):
        current = self.head
        stone_array = []
        while current:
            stone_array.append(current.val)
            current = current.next

        print(f"{stone_array}")

    def display_full(self):
        current = self.head
        while current:
            print(f"Stone(val={current.val}, prev={current.prev.val if current.prev else None}, next={current.next.val if current.next else None})")
            current = current.next

def pt1(param):
    BLINKS = 25
    ll = LinkedList(param)

    print("Before blinking:")
    ll.display()

    for i in range(BLINKS):
        ll.blink()

        print(f"\nAfter blinking {i} times:")
        ll.display()

    return ll.count_stones()
	

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day11.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    args = parser.parse_args()

    # Use the filename argument

    parsed_input = parse_input(args.filename)
    print(parsed_input)

    part1_answer = pt1(parsed_input)

    print(f"Part 1: total = {part1_answer}")
