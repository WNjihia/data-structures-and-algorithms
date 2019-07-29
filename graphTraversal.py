class Graph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        if vertex in self.adjacencyList:
            return "Vertex already exists"

        self.adjacencyList[vertex] = []

    def addEdge(self, vertex1, vertex2):
        if vertex1 not in self.adjacencyList:
            return "Vertex does not exist"

        if vertex2 not in self.adjacencyList:
            return "Vertex does not exist"

        # Undirected graph
        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)

    def removeEdge(self, vertex1, vertex2):
        if vertex1 not in self.adjacencyList:
            return "Vertex does not exist"

        if vertex2 not in self.adjacencyList:
            return "Vertex does not exist"

        # Undirected graph
        if vertex2 in self.adjacencyList[vertex1]:
            self.adjacencyList[vertex1].remove(vertex2)

        if vertex1 in self.adjacencyList[vertex2]:
            self.adjacencyList[vertex2].remove(vertex1)

    def removeVertex(self, vertex):
        if vertex not in self.adjacencyList:
            return "Vertex does not exist"

        while self.adjacencyList[vertex] != []:
            self.removeEdge(vertex, self.adjacencyList[vertex].pop())

        del self.adjacencyList[vertex]

    def dfsRecursive(self, sVertex):
        visited = {}
        result = []

        def dfsHelper(vertex):
            if not vertex:
                return None

            if vertex not in self.adjacencyList:
                return "Vertex does not exist"

            visited[vertex] = True
            result.append(vertex)

            for neighbor in self.adjacencyList[vertex]:
                if neighbor not in visited:
                    return dfsHelper(neighbor)

        dfsHelper(sVertex)

        return result

    def dfsIterative(self, sVertex):
        stack = [sVertex]
        visited = {}
        result = []

        visited[sVertex] = True

        while stack != []:
            v = stack.pop()
            result.append(v)
            for neighbor in self.adjacencyList[v]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    stack.append(neighbor)
        return result

    def bfs(self, sVertex):
        queue = [sVertex]
        visited = {}
        result = []

        visited[sVertex] = True

        while queue != []:
            v = queue.pop()
            result.append(v)
            for neighbor in self.adjacencyList[v]:
                if neighbor not in visited:
                    queue.insert(0, neighbor)
                    visited[neighbor] = True
        return result


g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
# g.addVertex("F")
g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "D")
g.addEdge("C", "E")
g.addEdge("D", "E")
# g.addEdge("D", "F")
# g.addEdge("E", "F")

for key, value in g.adjacencyList.items():
    print(key, value)

print(g.dfsRecursive("A"))
print(g.dfsIterative("A"))
print(g.bfs("A"))
