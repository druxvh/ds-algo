class Node:
    def __init__(self, item = None):
        self.item = item
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.recursive_insert_func(self.root, data)

    def recursive_insert_func(self, root, data):
        if root is None:
            return Node(data)

        if data < root.item:
            root.left = self.recursive_insert_func(root.left, data)
        elif data > root.item:
            root.right = self.recursive_insert_func(root.right, data)
        return root

    def search(self, data):
        return self.recursive_search(self.root, data)
    
    def recursive_search(self, root, data):
        if root is None or root.item == data:
            return root
        
        if data < root.item:
            return self.recursive_search(root.left, data)
        elif data > root.item:
            return self.recursive_search(root.right, data)
        
    def inorder(self):
        result = []
        self.recursive_inorder(self.root, result)
        return result
    
    def recursive_inorder(self, root, result):
        if root:
            self.recursive_inorder(root.left, result)
            result.append(root.item)
            self.recursive_inorder(root.right, result)
        
    def preorder(self):
        result = []
        self.recursive_preorder(self.root, result)
        return result
    
    def recursive_preorder(self, root, result):
        if root:
            result.append(root.item)
            self.recursive_preorder(root.left, result)
            self.recursive_preorder(root.right, result)
            
    def postorder(self):
        result = []
        self.recursive_postorder(self.root, result)
        return result
    
    def recursive_postorder(self, root, result):
        if root:
            self.recursive_postorder(root.left, result)
            self.recursive_postorder(root.right, result)
            result.append(root.item)

    def min_val(self, temp):
        current_point = temp
        while current_point.left is not None:
            current_point = current_point.left
        return current_point.item
    
    def max_val(self, temp):
        current_point = temp
        while current_point.right is not None:
            current_point = current_point.right
        return current_point.item
    
    def delete(self, data):
        self.root = self.recursive_deletion(self.root, data)

    def recursive_deletion(self, root, data):
        if root is None:
            return None
        
        if data < root.item:
            root.left = self.recursive_deletion(root.left, data)
        elif data > root.item:
            root.right = self.recursive_deletion(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_val(root.right)
            root.right = self.recursive_deletion(root.right, root.item)
        return root
        
    def size(self):
        return len(self.inorder())


'''
m = BST()
m.insert(10)
m.insert(20)
m.insert(110)
m.insert(1450)
m.insert(1)
m.insert(40)

print(m.size())
'''