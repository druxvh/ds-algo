
class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data
    
    def __repr__(self):
        return '<Node Data: %s>' % self.data
    
class CLL:
    def __init__(self):
        self.tail = None
    
    def is_empty(self):
        return self.tail == None
    
    def insert_at_start(self, data):
        if not data:
            return 'Error, no data entered'

        n = Node(data)
        
        if self.is_empty():
            n.next_node = n     #since its empty, the next will ref to itself since its a CLL
            self.tail = n
        else:
            n.next_node = self.tail.next_node
            self.tail.next_node = n
        
    def insert_at_last(self, data):
        if not data:
            return 'Error, no data entered'

        n = Node(data)
        
        if self.is_empty():
            n.next_node = n     
            self.tail = n
        else:
            n.next_node = self.tail.next_node
            self.tail.next_node = n
            self.tail = n

    def insert_after(self, temp, data):
        if not data or temp is None:
            return 'Error, temp or data is missing'
        
        if self.is_empty():
            return 'List is empty'


        search_node = self.search(temp)
        if search_node is None:
            return "error"
        
        n = Node(data)
        n.next_node = search_node.next_node
        search_node.next_node = n

        if search_node == self.tail:
            self.tail = n

    def del_first(self):
        if self.is_empty():
            return 'List is empty'
        
        if self.tail.next_node == self.tail:
            self.tail = None
        else:       
            self.tail.next_node = self.tail.next_node.next_node
        
    def del_last(self):
        if self.is_empty():
            return 'List is empty'
        
        if self.tail.next_node == self.tail:
            self.tail = None
        else:
            temp = self.tail.next_node
            while temp.next_node is not self.tail:
                temp = temp.next_node

            temp.next_node = self.tail.next_node
            self.tail = temp

    def delete(self, data):
        if self.is_empty():
            return 'List is empty'
        
        #if one node only and it contains data
        if self.tail.next_node == self.tail:
            if self.tail.data == data:
                self.tail = None
                return

        #if head contains data
        if self.tail.next_node.data == data:
            self.del_first()
            return
         
        temp = self.tail.next_node
        while temp.next_node is not self.tail:
            if temp.next_node.data == data:
                temp.next_node = temp.next_node.next_node
                break
            temp = temp.next_node

        #if tail contains data
        if self.tail.data == data:
            self.del_last() 
        return 'Not found'

    def search(self, data):

        if data is None:
            return 'Error, no data'
        
        if self.is_empty():
            return 'List is empty'
        
        if self.tail == self.tail.next_node:
            if self.tail.data == data:
                return self.tail

        temp = self.tail.next_node
        while temp is not self.tail:
            if temp.data == data:
                return temp
            temp = temp.next_node    
        if temp.data == data:
            return temp
        return None
    
    def print(self):
        if self.is_empty():
            return 'List empty'

        temp = self.tail.next_node
        while temp != self.tail:
            print(temp.data, end=" -> ")
            temp = temp.next_node
        print(temp.data)

    def __iter__(self):
        if self.tail == None:
            return CLL_Iterator(None)
        else:
            return CLL_Iterator(self.tail.next_node)

class CLL_Iterator:
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.data
        self.current = self.current.next_node
        
        return data
    
