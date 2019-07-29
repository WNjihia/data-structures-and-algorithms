class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, val):
        self.items.append(val)
        return self.items

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        self.items.pop()
        return self.items

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.items[-1]

stack = Stack()
print(stack.pop())
print(stack.push("12"))
stack.push("15")
stack.push("200")
print(stack.peek())
print(stack.pop())
