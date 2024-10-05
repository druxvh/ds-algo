class Heap:
    def __init__(self):
        self.heap = []

    def createHeap(self, arr):
        for val in arr:
            self.insert(val)
    
    def insert(self, val):
        self.heap.append(val) # --> appends the value into the last of an array
        index = len(self.heap) - 1 # --> last element (the recently appended val)
        self.upheap(index)
    
    def upheap(self, index):
        if len(self.heap) == 0:
            return
        parent = self.parent(index)
        if index > 0 and self.heap[parent] < self.heap[index]:
            self.swap(index, parent)
            self.upheap(parent)   
        
    def delete(self):
        if len(self.heap) == 0:
            raise EmptyHeadException()
            
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.downheap(0)

        return max_val

    def downheap(self, index):
        left = self.leftChild(index)
        right = self.rightChild(index)
        largest = index

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.swap(largest, index)
            self.downheap(largest)

    def heapSort(self, arr):
        self.createHeap(arr)
        data = []

        while len(self.heap) > 0:
            data.insert(0, self.delete())

        return data


    def top(self):
        if len(self.heap) == 0:
            raise EmptyHeadException()
        return self.heap[0]

    def leftChild(self, index):
        return (2 * index) + 1

    def rightChild(self, index):
        return (2 * index) + 2
    
    def parent(self, index):
        return (index - 1) // 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def print_heap(self):
        print(self.heap)


class EmptyHeadException(Exception):
    def __init__(self):
        msg = 'Empty Head'
        self.msg = msg

    def __str__(self):
        return self.msg

