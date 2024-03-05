class ArrayStack:
    """LIFO Stack implementation using a list"""
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def top(self):
        """Return the top element of the stack and does not delete it""" 
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data[-1]

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.data.pop()
