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

    def bfs(self):
        if self.root is None:
            return "Tree is empty"

        queue = []
        visited = []
        queue.insert(0, self.root)

        while queue != []:
            current = queue[-1]
            if current.left:
                queue.insert(0, current.left)
            if current.right:
                queue.insert(0, current.right)
            visited.append(queue[-1].value)
            queue.pop()

        return visited

    def dfs_preOrder(self):
        visited = []

        def traverse(node):
            visited.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)

        traverse(self.root)

        return visited

    def dfs_postOrder(self):
        visited = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
            visited.append(node.value)

        traverse(self.root)

        return visited

    def dfs_inOrder(self):
        visited = []

        def traverse(node):
            if node.left:
                traverse(node.left)
            visited.append(node.value)
            if node.right:
                traverse(node.right)

        traverse(self.root)

        return visited


tree = BST()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)
print(tree.bfs())
print(tree.dfs_preOrder())
print(tree.dfs_postOrder())
print(tree.dfs_inOrder())
