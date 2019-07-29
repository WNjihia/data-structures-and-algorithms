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

        # Directed Graph
        # self.adjacencyList[vertex1].append(vertex2)

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

        # Directed Graph
        # if vertex2 in self.adjacencyList[vertex1]:
        #     self.adjacencyList[vertex1].remove(vertex2)

    def removeVertex(self, vertex):
        if vertex not in self.adjacencyList:
            return "Vertex does not exist"

        while self.adjacencyList[vertex] != []:
            self.removeEdge(vertex, self.adjacencyList[vertex].pop())

        del self.adjacencyList[vertex]


g = Graph()
g.addVertex("Dallas")
g.addVertex("Tokyo")
g.addVertex("Aspen")
g.addVertex("Los Angeles")
g.addVertex("Hong Kong")
g.addEdge("Dallas", "Tokyo")
g.addEdge("Dallas", "Aspen")
g.addEdge("Hong Kong", "Tokyo")
g.addEdge("Hong Kong", "Dallas")
g.addEdge("Los Angeles", "Hong Kong")
g.addEdge("Los Angeles", "Aspen")
g.removeEdge("Dallas", "Tokyo")
g.removeVertex("Hong Kong")

for key, value in g.adjacencyList.items():
    print(key, value)
