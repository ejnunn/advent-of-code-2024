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

    def display(self, return_true=False):
        current = self.head
        stone_array = []
        while current:
            stone_array.append(current.val)
            current = current.next

        # print(f"{stone_array}")
        
        if return_true:
            return stone_array    

    def display_full(self):
        current = self.head
        while current:
            print(f"Stone(val={current.val}, prev={current.prev.val if current.prev else None}, next={current.next.val if current.next else None})")
            current = current.next

def snapshot(linked_list, i):
    # Use a fixed extension for consistency
    prefix = "iteration_"
    extension = "txt"  # Removed the unnecessary period in the variable
    filename = f"{prefix}{i}.{extension}"  # Updated to use proper concatenation

    # Get the linked list elements as an array
    linked_list_array = linked_list.display(return_true=True)

    # Convert the array elements to a single string, space-separated
    content = " ".join(map(str, linked_list_array))  # Ensure elements are strings

    # Save the content to a new file
    with open(filename, 'w') as file:
        file.write(content)

    print(f"Saved to file: {filename}")
    return None


def pt2(param, blinks):
    ll = LinkedList(param)

    # print("Before blinking:")
    # ll.display()

    for i in range(1, blinks+1):
        ll.blink()
        # print(f"Blink count: {i}, Stone count: {ll.count_stones()}")
        # ll.display()

        # Save snapshot (10, 20, 30)
        if i % 5 == 0:
            # print(f"Saving snapshot. Iteration: {i}.")
            snapshot(ll, i)

    # print(f"After blinking {blinks} times. Stone_count = {ll.count_stones()}")


    return ll.count_stones()
	

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Process an input file for day11.")
    parser.add_argument('filename', type=str, help="The path to the input text file.")
    parser.add_argument('blinks', type=int, help="The number of blinks to perform.")
    args = parser.parse_args()

    # Use the filename argument
    parsed_input = parse_input(args.filename)
    blinks = args.blinks

    part2_answer = pt2(parsed_input, blinks)

    print(f"Part 2: total = {part2_answer}")
