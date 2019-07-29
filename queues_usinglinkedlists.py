class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        newNode = Node(value)
        if self.size == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return "Queue is Empty"
        dequeuedItem = self.first
        self.first = dequeuedItem.next
        dequeuedItem.next = None
        self.size -= 0
        return dequeuedItem.value

    def peek(self):
        if self.size == 0:
            return "Queue is Empty"
        return self.first.value

    def traverse(self):
        if self.size == 0:
            return "Queue is Empty"
        printValue = self.first
        while printValue != None:
            print(printValue.value)
            printValue = printValue.next

queue = Queue()
queue.enqueue("50")
queue.enqueue("302")
queue.enqueue("2")
queue.traverse()
print(queue.peek())
queue.dequeue()
queue.traverse()
