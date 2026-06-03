class GraphAdjList:
    def __init__(self, vertices):
        self.V = vertices
        self.list_undirected = {i: [] for i in range(vertices)}
        self.list_directed = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        # For undirected graph
        self.list_undirected[u].append(v)
        self.list_undirected[v].append(u)
        
        # For directed graph
        self.list_directed[u].append(v)

    def display(self):
        print("Adjacency Undirected List:")
        for vertex in self.list_undirected:
            print(f"{vertex} -> {self.list_undirected[vertex]}")
            
        print("\nAdjacency Directed List:")
        for vertex in self.list_directed:
            print(f"{vertex} -> {self.list_directed[vertex]}")

# Create graph
g = GraphAdjList(5)

# Add edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(3, 4)

# Display
g.display()