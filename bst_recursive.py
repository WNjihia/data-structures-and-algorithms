class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None


    def insertHelper(self, current, value):
        if value == current.value:
            return "Item already added"

        if value < current.value:
            if current.left == None:
                current.left = Node(value)
            else:
                return self.insertHelper(current.left, value)

        if value > current.value:
            if current.right == None:
                current.right = Node(value)
            else:
                return self.insertHelper(current.right, value)


    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return;

        current = self.root
        return self.insertHelper(current, value)

    def find(self, current, value):
        if current is None:
            return False

        if current.value == value:
            return True

        if value < current.value:
            return self.find(current.left, value)

        return self.find(current.right, value)

    def contains(self, value):
        if self.root is None:
            return "Tree is empty"

        current = self.root
        return self.find(current, value)


tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(13)
tree.insert(2)
tree.insert(7)
tree.insert(11)
tree.insert(16)
print("Find:")
print(tree.contains(13))
print(tree.contains(50))
print(tree.contains(2))
print(tree.contains(0))
