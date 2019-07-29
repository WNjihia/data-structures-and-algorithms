class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        self.length += 1

    def unshift(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def pop(self):
        if self.length == 0:
            return "List is empty"

        toBePopped = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = toBePopped.previous
            self.tail.next = None
            toBePopped.previous = None
        self.length -= 1
        return toBePopped

    def shift(self):
        if self.length == 0:
            return "List is empty"

        toBeShifted = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = toBeShifted.next
            self.head.previous = None
            toBeShifted.next = None
        self.length -= 1
        return toBeShifted

    def traverse(self):
        pass

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        if index <= (self.length/2):
            start = self.head
            i = 0
            while i < index:
                current = start.next
                i += 1
            return current
        else:
            start = self.tail
            i = self.length - 1
            while i > index:
                current = start.previous
                i -= 1
            return current

    def set(self, value, index):
        node = self.get(index)
        if node == None:
            return False
        node.value = value
        return True


    def insert(self, value, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.unshift(val)
        if index == self.length:
            return self.push(val)

        newNode = Node(value)
        beforeNode = self.get(index - 1)
        afterNode = current.next

        newNode.previous = beforeNode
        newNode.next = afterNode

        beforeNode.next = newNode
        afterNode.previous = newNode
        self.length += 1

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.shift()
        if index == self.length - 1:
            return self.pop()

        current = self.get(index)
        beforeNode = current.previous
        afterNode = current.next

        beforeNode.next = afterNode
        afterNode.previous = beforeNode
        current.next = current.previous = None
        self.length -= 1
        return current
