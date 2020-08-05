'''A simple stack implementation in python using 3 approaches

    1) List Stack: O(1) for pops and pushes.
    2) Deque Stack: O(1) for pops and pushes.
    3) Linked-List Stack: O(1) for pops and pushes.

    A note about performance: List and Deque stacks perform similarly and are faster than the Linked-List version.

    API:
    class list_stack
              list_stack()        create an emtpy list stack
    bool      push(item)          insert a new item into the stack
    itemType  pop()               remove and return the item most recently added
    int       get_length()        returns the number of items in the stack

    class deque_stack
              deque_stack()       create an emtpy deque stack
    bool      push(item)          insert a new item into the stack
    itemType  pop()               remove and return the item most recently added
    int       get_length()        returns the number of items in the stack

    class ll_stack
              ll_stack()          create an emtpy linked list stack
    bool      push(item)          insert a new item into the stack
    itemType  pop()               remove and return the item most recently added
    int       get_length()        returns the number of items in the stack

    All stacks are iterable. Note: iteration through a stack only returns the values in the stack (in the order they would be popped) but does not pop them.
'''

from collections import deque

class list_stack():
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        return True

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        raise ValueError('Emtpy Stack')

    def get_length(self):
        return len(self.stack)

    def __str__(self):
        retStr = '['
        for i in range(len(self.stack)):
            if i != len(self.stack) - 1:
                retStr += str(self.stack[i]) + ', '
            else:
                retStr += str(self.stack[i])
        retStr += ']'
        return retStr

    def __iter__(self):
        self.index = len(self.stack) - 1
        return self

    def __next__(self):
        if self.index >= 0:
            last_index = self.index
            self.index -= 1
            return self.stack[last_index]
        else:
            raise StopIteration

class deque_stack():
    def __init__(self):
        self.stack = deque()

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            raise ValueError('Empty Stack')

    def get_length(self):
        return len(self.stack)

    def __str__(self):
        retStr = '['
        for i in range(len(self.stack)):
            if i != len(self.stack) - 1:
                retStr += str(self.stack[i]) + ', '
            else:
                retStr += str(self.stack[i])
        retStr += ']'
        return retStr

    def __iter__(self):
        self.index = len(self.stack) - 1
        return self

    def __next__(self):
        if self.index >= 0:
            last_index = self.index
            self.index -= 1
            return self.stack[last_index]
        else:
            raise StopIteration


class Node(object):
    def __init__(self, val, nn):
        self.val = val
        self.nn = nn

    def get_nn(self):
        return self.nn

    def set_nn(self, n):
        self.nn = n

    def get_val(self):
        return self.val

    def set_val(self, v):
        self.val = v

class ll_stack(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def push(self, val):
        if self.root is None:
            self.root = Node(val, None)
        else:
            new_node = Node(val, self.root)
            self.root = new_node
        self.size += 1
        return val

    def pop(self):
        if self.root is not None:
            val = self.root.get_val()
            next_node = self.root.get_nn()
            self.root = next_node
            self.size -= 1
            return val
        else:
            raise ValueError("Empty Stack")

    def get_length(self):
        return self.size

    def __str__(self):
        retStr = "["
        this_node = self.root
        while this_node is not None:
            if this_node != self.root:
                retStr += ', ' + str(this_node.get_val())
            else:
                retStr += str(this_node.get_val())
            this_node = this_node.get_nn()
        retStr += ']'
        return retStr

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.size:
            this_node = self.root
            last_index = self.index
            self.index += 1
            for i in range(0, last_index):
                this_node = this_node.get_nn()
            return this_node.get_val()
        else:
            raise StopIteration


