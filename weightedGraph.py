class WeightedGraph:
    def __init__(self):
        self.adjacencyList = {}

    def addVertex(self, vertex):
        if vertex in self.adjacencyList:
            return "Vertex already exists"

        self.adjacencyList[vertex] = []

    def addEdge(self, vertex1, vertex2, weight):
        if vertex1 not in self.adjacencyList:
            return "Vertex does not exist"

        if vertex2 not in self.adjacencyList:
            return "Vertex does not exist"

        # Undirected graph
        self.adjacencyList[vertex1].append({vertex2, weight})
        self.adjacencyList[vertex2].append({vertex1, weight})


g = WeightedGraph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addEdge("A", "B", 9)
g.addEdge("A", "D", 3)
g.addEdge("A", "C", 5)
g.addEdge("B", "C", 7)

print(g.adjacencyList)
