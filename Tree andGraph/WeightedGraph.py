class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


g = WeightedGraph()
g.add_edge('A', 'B', 2)
g.add_edge('A', 'C', 5)
g.add_edge('B', 'C', 1)

g.display()