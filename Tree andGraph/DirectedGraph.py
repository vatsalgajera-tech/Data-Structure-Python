class DirectedGraph:
    def __init__(self):
        self.graph = {}

    # -------- ADD VERTEX --------
    def add_vertex(self, v):
        if v not in self.graph:
            self.graph[v] = []
        else:
            print("Vertex already exists")

    # -------- REMOVE VERTEX --------
    def remove_vertex(self, v):
        if v not in self.graph:
            print("Vertex not found")
            return

        # Remove incoming edges
        for key in self.graph:
            if v in self.graph[key]:
                self.graph[key].remove(v)

        # Remove vertex
        del self.graph[v]

    # -------- ADD EDGE --------
    def add_edge(self, u, v):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)

        self.graph[u].append(v)
        # self.graph[v].append(u)

    # -------- REMOVE EDGE --------
    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)

    # -------- DISPLAY --------
    def display(self):
        for v in self.graph:
            print(f"{v} -> {self.graph[v]}")


# -------- TEST --------
g = DirectedGraph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)

g.display()

print("\nRemove edge (0 -> 2)")
g.remove_edge(0, 2)

print("\nRemove vertex (1)")
g.remove_vertex(1)

g.display()