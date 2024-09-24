class Graph:
    def __init__(self, vertex_no):
        self.vertex_count = vertex_no
        self.adj_matrix = [ [0]*vertex_no for e in range(vertex_no) ]     # '*' is a repetition operator here

    def add_edge(self, u, v, weight = 1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = weight
            self.adj_matrix[v][u] = weight
        else:
            print("Invalid Vertex")

    def remove_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_matrix[u][v] = 0
            self.adj_matrix[v][u] = 0
        else:
            print("Invalid Vertex")

    def has_edge(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return self.adj_matrix[u][v] is not 0
        else:
            print("Invalid Vertex")

    def print_matrix(self):
        for row in self.adj_matrix:
            print(" ".join(map(str, row)))

'''
g = Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)

g.print_matrix()
'''