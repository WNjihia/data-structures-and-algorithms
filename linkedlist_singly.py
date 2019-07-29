class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Add node at the end of the list
    def push(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    # Add node at the beginning of the list
    def unshift(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    # Remove node at the end of the list
    def pop(self):
        if self.length == 0:
            return "List is empty"

        current = self.head
        preCurrent = None

        while current.next != None:
            preCurrent = current
            current = current.next
        self.tail = preCurrent
        self.tail.next = None
        self.length -= 1
        return current.val

    # Remove node at the beginning of the list
    def shift(self):
        if self.length == 0:
            return "List is empty"

        current = self.head
        self.head = self.head.next
        self.length -= 1
        return current

    # Traverses the list
    def traverse(self):
        if self.length == 0:
            return "List is Empty"
        printValue = self.head
        while printValue != None:
            print(printValue.val)
            printValue = printValue.next

    # Retrieves the node at specific position
    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        counter = 0
        currentNode = self.head

        while counter != index:
            currentNode = currentNode.next
            counter += 1

        return currentNode

    # Change value of node based on its position
    def set(self, index, val):
        node = self.get(index)
        if node != None:
            node.val = val
            return True
        return False

    # Add node at specific position
    def insert(self, val, index):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.unshift(val)
        if index == self.length:
            return self.push(val)

        newNode = Node(val)
        prevNode = self.get(index-1)
        newNode.next = prevNode.next
        prevNode.next = newNode
        self.length += 1

    # Remove node at specific position
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.shift()
        if index == self.length-1:
            return self.pop()

        prevNode = self.get(index-1)
        node = prevNode.next
        prevNode.next = node.next
        return node

    # Reverse list in place
    def reverse(self):
        current = self.head
        prevNode = None
        while current != None:
            nextNode = current.next
            current.next = prevNode
            prevNode = current
            current = nextNode
        self.head = prevNode

    # delete duplicate values in sorted list
    def deleteDuplicates(self):
        node = self.head
        while node.next:
            next = node.next
            if node.val == next.val:
                next = next.next
                node.next = next
            else:
                node = next

    def mergeSortedlist(self, l1, l2):
        # method 1
        temp = None
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val <= l2.val:
                temp = l1
                temp.next = self.mergeSortedlist(l1.next, l2)
            else:
                temp = l2
                temp.next = mergeSortedlist(l1, l2.next)
            return temp

        # method 2
            # if l1 and l2:
            #     if l1.val <= l2.val:
            #         newNode = ListNode(l1.val)
            #         l1 = l1.next
            #     else:
            #         newNode = ListNode(l2.val)
            #         l2 = l2.next
            # elif l1:
            #     newNode = ListNode(l1.val)
            #     l1 = l1.next
            # elif l2:
            #     newNode = ListNode(l2.val)
            #     l2 = l2.next
            # else:
            #     return None
            #
            # nextNode = merge(l1, l2)
            #
            # if nextNode:
            #     newNode.next = nextNode
            # return newNode

list = SinglyLinkedList()
list.push("10")
list.push("129")
list.push("12")
list.unshift("109")
list.insert("64", 1)
list.pop()
list.shift()
list.push("32")
list.push("45")
list.remove(2)
list.reverse()
list.traverse()
