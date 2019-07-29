# Min Binary Heap

class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def bubbleUp(self, queue):
        index = len(queue) - 1
        parentIndex = (index - 1) // 2

        while index > 0 and queue[index].priority < queue[parentIndex].priority:
            queue[index], queue[parentIndex] = queue[parentIndex], queue[index]
            index = parentIndex
            parentIndex = (index - 1) // 2
        return queue

    def enqueue(self, value, priority):
        newNode = Node(value, priority)
        self.queue.append(newNode)
        self.bubbleUp(self.queue)

    def bubbleDown(self, queue):
        index = 0
        length = len(queue)

        while True:
            left = (2 * index) + 1
            right = (2 * index) + 2
            temp = None

            if left < length:
                if queue[left].priority < queue[index].priority:
                    temp = left

            if right < length:
                if queue[right].priority < queue[index].priority and \
                   queue[right].priority < queue[left].priority:
                    temp = right

            if temp == None:
                break;

            queue[index], queue[temp] = queue[temp], queue[index]
            index = temp

    def dequeue(self):
        if self.queue == []:
            return "Queue is empty"

        min = self.queue[0]
        end = self.queue.pop()

        if self.queue != []:
            self.queue[0] = end
            self.bubbleDown(self.queue)

        return min


queue = PriorityQueue()
queue.enqueue("common cold", 5)
queue.enqueue("gunshot wound", 1)
queue.enqueue("high fever", 4)
queue.enqueue("broken arm", 2)
queue.enqueue("glass in foot", 3)
queue.dequeue()
queue.dequeue()
queue.dequeue()
