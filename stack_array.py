"""Stack Array Implementation for Project 2
Course: CPE202
Quarter: Spring 2020
Author: Chris Linthacum
"""


class StackArray:
    """ An implementation of the Stack ADT using an array
    Attributes:
        arr(array): The array of items stored in the stack
        capacity(int): The total capacity of the current array
        num_items(int): The number of items currently stored in the stack

    Methods:
        pop():
        push():
        peek():
        is_empty():
        size():
    """

    def __init__(self):
        """Initialize the stack by creating an array of size two containing
           two Nones
        """
        self.arr = [None] * 2
        self.capacity = 2
        self.num_items = 0

    def __repr__(self):
        """How the stack is represented when printed"""

        # Can just pass array to str()
        array_out = ''
        for i in range(self.num_items - 1):
            array_out += str(self.arr[i])
            array_out += ' '
        array_out += str(self.arr[self.num_items - 1])
        return array_out

    def __eq__(self, other):
        """Is stack is the same as another stack
        Args:
            other(StackArray): another StackArray instance being compared against
        Returns:
            bool: True if stacks equal. False if otherwise.
        """

        return isinstance(other, StackArray) and other.num_items == self.num_items and \
            other.arr == self.arr

    def enlarge(self):
        """Function to enlarge the size of array by 2 when capacity reached
        """

        new_array = [None] * (self.capacity * 2)
        if self.capacity == self.num_items:
            for i in range(self.num_items):
                new_array[i] = self.arr[i]
            self.arr = new_array
            self.capacity = self.capacity * 2

    def shrink(self):
        """Function to reduce size of the array by factor of 2 when
           capacity / num_items >= 4
        """

        if self.num_items == 0 or self.capacity / self.num_items >= 4:
            new_array = [None] * (self.capacity // 2)
            for i in range(self.num_items):
                new_array[i] = self.arr[i]
            self.arr = new_array
            self.capacity = self.capacity // 2

    def pop(self):
        """Function to remove the top item from the stack. Stack is modified.
        Args:
            None
        Returns:
            any: the top item from the stack
        """

        if self.num_items == 0:
            raise IndexError('Stack is empty.')
        return_item = self.arr[self.num_items - 1]
        self.num_items -= 1
        self.shrink()
        return return_item

    def push(self, item):
        """Function to push an item on the top of a stack.
        Args:
            item(any): item being added to the top of the stack
        Returns:
            None
        """

        self.arr[self.num_items] = item
        self.num_items += 1
        self.enlarge()

    def peek(self):
        """Function to return top item from the stack. Does not remove item.
        Args:
            None
        Returns:
            any: top item from the stack
        """
        if self.num_items == 0:
            raise IndexError('Stack is empty.')
        return self.arr[self.num_items - 1]

    def is_empty(self):
        """Function to check whether or not the stack is empty
        Args:
            None
        Returns:
            bool: True if stack is empty. False if otherwise.
        """

        return self.num_items == 0

    def size(self):
        """Function to return the current size of the stack.
        Args:
            None
        Returns:
            int: number of items on the stack
        """

        return self.num_items
