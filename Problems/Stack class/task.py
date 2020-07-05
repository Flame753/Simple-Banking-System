class Stack():

    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        popped = self.stack[-1]
        self.stack.remove(self.stack[-1])
        return popped

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return self.stack == []
