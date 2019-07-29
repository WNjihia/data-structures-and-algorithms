import math


class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def bubbleUp(self, queue):
        index = len(queue) - 1
        parentIndex = (index - 1) // 2

        while index > 0 and queue[index].priority < queue[parentIndex].priority:
            queue[index], queue[parentIndex] = queue[parentIndex], queue[parentIndex]
            index = parentIndex
            parentIndex = (index - 1) // 2

        return queue

    def bubbleDown(self, queue):
        index = 0
        length = len(queue)

        while True:
            left = (2*index) + 1
            right = (2*index) + 2
            temp = None

            if left < length:
                if queue[left].priority < queue[index].priority:
                    temp = left

            if right < length:
                if queue[right].priority < queue[index].priority and \
                   queue[right].priority < queue[left].priority:
                    temp = right

            if not temp:
                break;

            queue[index], queue[temp] = queue[temp], queue[index]
            index = temp

    def enqueue(self, value, priority):
        newNode = Node(value, priority)
        # if node in queue:
        #     node.priority = priority
        for node in self.queue:
            if node.val == value
        self.queue.append(node)
        self.bubbleUp(self.queue)

    def dequeue(self):
        if self.queue == []:
            return "Queue is empty"

        smallest = self.queue[0]
        last = self.queue.pop()

        self.queue[0] = last
        self.bubbleDown(self.queue)

        return smallest


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
        self.adjacencyList[vertex1].append((vertex2, weight))
        self.adjacencyList[vertex2].append((vertex1, weight))

    def dijkstra(self, startV, endV):
        pQueue = PriorityQueue()
        previous = {}
        distances = {}
        path = []

        for key, value in self.adjacencyList.items():
            # Initialize pQueue, distances and previous
            if key == startV:
                distances[key] = 0
                pQueue.enqueue(startV, 0)
            else:
                distances[key] = math.inf
                pQueue.enqueue(key, math.inf)

            previous[key] = None

        while pQueue.queue != []:
            for val in pQueue.queue:
                print(val.val, val.priority)
            shortest = pQueue.dequeue() # A C
            print(shortest.val)

            # Check if we've visited all vertices till the endV
            # if shortest.val == endV:
            #     shortestVal = shortest.val
            #     while previous[shortestVal]:
            #         path.append(shortestVal)
            #         shortestVal = previous[shortestVal]
            #     path.append(shortestVal)
            #     return path[::-1]

            # Visit neighbouring nodes
            # for vertex in self.adjacencyList[shortest.val]:
            #     v, weight = vertex # B 4, C 2 | D 2, F 4
            #     # Calculate distance to neighbouring node from startV
            #     vDistance = weight + distances[shortest.val] # 4+0 2+0 | 2+2 4+2
            #     # Compare distances and update previous
            #     if vDistance < distances[v]:
            #         # Update new shortest distance to neighbor
            #         distances[v] = vDistance #{b: 4, c:2, d:4, f:6}
            #         # Update previous - how we got to neighbor
            #         previous[v] = shortest.val # {b: a c:a, d:c, f:c}
            #         pQueue.enqueue(v, vDistance) # b,4 c,2 d,4, f,6
            #     # print(distances)

g = WeightedGraph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.addEdge("A", "B", 4)
g.addEdge("A", "C", 2)
g.addEdge("C", "D", 2)
g.addEdge("C", "F", 4)
g.addEdge("B", "E", 3)
g.addEdge("D", "E", 3)
g.addEdge("D", "F", 1)
g.addEdge("E", "F", 1)

print(g.adjacencyList)

print(g.dijkstra("A", "E"))
