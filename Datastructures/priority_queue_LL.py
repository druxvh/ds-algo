class Node:
    '''
    item as your item/data and priority number for its order.
    '''
    def __init__(self, item = None, priority = None):
        self.item = item
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count == 0

    def push(self, data, priority):
        if not data or priority is None:
            raise SyntaxError("Data or Priority is missing")
        
        n = Node(data, priority)
        if self.is_empty() or priority < self.start.priority:
            n.next = self.start
            self.start = n
        else:
            temp = self.start

            while temp.next is not None and temp.next.priority <= priority:
                temp = temp.next

            n.next = temp.next
            temp.next = n
        self.item_count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Empty Queue")
        data = self.start.item
        self.start = self.start.next
        self.item_count -= 1
        return data
    
    def size(self):
        return self.item_count

'''
d = PriorityQueue()
d.push("one", 1)
d.push("three", 3)
d.push("two", 2)
d.push("eleven", 11)
d.push("four", 4)

while not d.is_empty():
    print(d.pop())
'''  