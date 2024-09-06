class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self, data, priority):
        index = 0
        while index < len(self.items) and self.items[index][1] <= priority:
            index += 1
        self.items.insert(index, (data, priority))
    
    def pop(self):
        if self.is_empty():
            raise IndexError("Priority Queue Empty")
        return self.items.pop(0)[0]
    
    def size(self):
        return len(self.items)


'''
d = PriorityQueue()
d.push("haah", 9)
d.push("heehee", 1)
d.push("ttwo", 2)
d.push("hefrevcerfehee", 11)
d.push("aaseee", 4)

while not d.is_empty():
    print(d.pop())
''' 