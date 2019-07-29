class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.append(0, item)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items[-1]
