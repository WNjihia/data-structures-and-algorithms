# Insert and Find Iteratively


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            return

        current = self.root
        while True:
            if value == current.value:
                return "Item already added"

            if value < current.value:
                if current.left == None:
                    current.left = newNode
                    return
                else:
                    current = current.left
            else:
                if current.right == None:
                    current.right = newNode
                    return
                else:
                    current = current.right

    def contains(self, value):
        if self.root == None:
            return "Tree is empty"

        current = self.root

        while current != None:
            if value == current.value:
                return True

            if value < current.value:
                current = current.left
            else:
                current = current.right

        return False

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
