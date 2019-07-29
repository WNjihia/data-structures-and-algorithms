class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def push(self, val):
        node = Node(val)
        if self.first == None:
            self.first = node
        else:
            node.next = self.first
            self.first = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return "Stack is empty"
        current = self.first
        self.first = current.next
        self.size -= 1

    def peek(self):
        if self.size == 0:
            return "Stack is empty"
        return self.first.val

    def traverse(self):
        if self.size == 0:
            return "Stack is Empty"
        printValue = self.first
        while printValue != None:
            print(printValue.val)
            printValue = printValue.next

stack = Stack()
stack.push("50")
stack.push("302")
stack.push("2")
stack.traverse()
print(stack.peek())
stack.pop()
stack.traverse()
