class GraphAdjMatrix:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix_undireted = [[0 for _ in range(vertices)] for _ in range(vertices)]
        self.matrix_direted = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def add_edge(self, u, v):
        # Undirected graph
        self.matrix_undireted[u][v] = 1
        self.matrix_undireted[v][u] = 1
        
        # Directed graph 
        self.matrix_direted[u][v] = 1 
                           
    
    def display(self):
        print("Adjacency Undirected Matrix:")
        for row in self.matrix_undireted:
            print(row)

        print("\nAdjacency Directed Matrix:")
        for row in self.matrix_direted:
            print(row)

# Create graph
g = GraphAdjMatrix(3)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(2, 2)

# Display
g.display()