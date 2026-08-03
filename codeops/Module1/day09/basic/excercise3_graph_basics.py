# Exercise 3: Graph Basics

class Graph:
    def __init__(self):
        self.connections = {}  # adjacency list: customer -> list of connected customers

    def add_customer(self, name):
        if name not in self.connections:
            self.connections[name] = []

    def add_transfer(self, person1, person2):
        # O(1) - just appends to two lists
        self.add_customer(person1)
        self.add_customer(person2)
        self.connections[person1].append(person2)
        self.connections[person2].append(person1)

    def print_graph(self):
        for person, links in self.connections.items():
            print(f"{person} -> {links}")


graph = Graph()
graph.add_customer("Almaz")
graph.add_customer("Dawit")
graph.add_customer("Tigist")
graph.add_customer("Hanna")

graph.add_transfer("Almaz", "Dawit")
graph.add_transfer("Dawit", "Tigist")
graph.add_transfer("Almaz", "Hanna")

graph.print_graph()