class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next_node = None

class CDLL:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def insert_at_start(self, data):
        n = Node(data)
        if self.is_empty():
            n.prev = n
            n.next_node = n
            self.head = n
        else:
            n.prev = self.head.prev
            n.next_node = self.head
            self.head.prev.next_node = n
            self.head.prev = n
            self.head = n

    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.prev = n
            n.next_node = n
            self.head = n
        else:
            n.prev = self.head.prev
            n.next_node = self.head
            self.head.prev.next_node = n
            self.head.prev = n

    def insert_after(self, temp, data):
        if not temp or data is None:
            return 'Error, temp value or data not entered'
        
        if not self.is_empty():
            n = Node(data)
            n.prev = temp
            n.next_node = temp.next_node
            temp.next_node.prev = n
            temp.next_node = n

    def del_first(self):
        if self.is_empty():
            return 'List is empty'
        
        #if only one node is their
        if self.head.next_node == self.head:
            self.head = None
        else:
            self.head.next_node.prev = self.head.prev
            self.head.prev.next_node = self.head.next_node
            self.head = self.head.next_node

    def del_last(self):
        if self.is_empty():
            return 'List is empty'
        
        #if only one node is their
        if self.head.next_node == self.head:
            self.head = None
        else:
            self.head.prev.prev.next_node = self.head
            self.head.prev = self.head.prev.prev


    def delete(self, data):
        if data is not None:
            temp = self.head
            if temp.data == data:
                self.del_first()
            else:
                while temp.next_node is not self.head:
                    if temp.data == data:
                        temp.prev.next_node = temp.next_node
                        temp.next_node.prev = temp.prev
                        return
                    temp = temp.next_node
                
                if temp.data == data:
                    self.del_last()


    def search(self, data):
        if self.head is None:
            return None
        
        temp = self.head
                
        while True:
            if temp.data == data:
                return temp
            temp = temp.next_node
            
            if temp == self.head:       #if temp reaches the first node since its circular, so breaking the loop
                break

        return None

    def print(self):
        if self.is_empty():
            return 'List is empty'

        temp = self.head

        if temp is not None:
            print(temp.data, end="  ")
            temp = temp.next_node
            while temp != self.head:
                print(temp.data, end="  ")
                temp = temp.next_node
            print()
            
    def __iter__(self):
        return CDLL_Iterator(self.head)

class CDLL_Iterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        
        if self.current == self.start and self.count ==1:
            raise StopIteration
        else:
            self.count = 1

        data = self.current.data
        self.current = self.current.next_node
        return data
        

dm = CDLL()
dm.insert_at_start(1)
dm.insert_at_start(2)
dm.insert_at_start(3)
dm.insert_at_last(4)
dm.insert_at_last(5)
dm.print()

# Testing the iterator
for value in dm:
    print(value, end="  ")
print()