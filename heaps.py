class MaxBinaryHeap:
    def __init__(self):
        self.values = [55,39,41,18,27,12,33]

    def bubbleUp(self, values):
        index = len(values) - 1
        parentIndex = (index-1) // 2

        while index > 0 and values[index] > values[parentIndex]:
            values[parentIndex], values[index] = values[index], values[parentIndex]
            index = parentIndex
            parentIndex = (index-1) // 2
        return values

    def insert(self, value):
        self.values.append(value)
        self.bubbleUp(self.values)

    def bubbleDown(self, values):
        index = 0
        length = len(values)

        while True:
            left = (2 * index) + 1
            right = (2 * index) + 2
            temp = None

            if left < length:
                if values[left] > values[index]:
                    temp = left

            if right < length:
                if values[right] > values[left] and values[right] > values[index]:
                    temp = right

            if temp == None:
                break;

            values[index], values[temp] = values[temp], values[index]
            index = temp


    def extractMax(self):
        if self.values == []:
            return "Heap is empty"

        max = self.values[0]
        end = self.values.pop()

        if self.values != []:
            self.values[0] = end
            self.bubbleDown(self.values)
        return max


heap = MaxBinaryHeap()
heap.insert(55)
# heap.insert(45)
print(heap.values)
# print(heap.extractMax())
# print(heap.values)
