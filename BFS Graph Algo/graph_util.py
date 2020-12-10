
class graph:
    """ This implements and adjacency list representation of a graph.
     It is designed for Nodes are represented as strings, but it will work if nodes are represented as any immutable type. The adjacency list is implemented as a dictionary from node labels to a set of adjacent node labels."""
    def __init__(self, nodes=[]):
        # creates a new graph. It is empty if no nodes list is provided, otherwise the graph will contain all the nodes in that list.
        self.adjacency_list = {}
        for node in nodes:
            self.adjacency_list[node] = set()
    
    def __str__(self):
        # Gives a string representation of the adjacency list
        rep = ""
        for node in self.adjacency_list:
            rep += str(node) + ": "
            rep += str(list(self.adjacency_list[node]))
            rep += '\n'
        return rep.strip()
    
    def __repr__(self):
        rep = ""
        for node in self.adjacency_list:
            rep += str(node) + ":"
            rep += str(list(self.adjacency_list[node]))
            rep += ';'
        return rep.strip(';')
    
    def add_node(self, node):
        # Add a new node to the graph, it will originally have an empty adjacency list
        if node in self.adjacency_list:
            return False
        self.adjacency_list[node] = set()
        return True
    
    def add_edge(self, nodea, nodeb):
        # Add a new edge to the graph. Since the graph is undirected, each node will be added to the other's adjacency list.
        self.adjacency_list[nodea].add(nodeb)
        self.adjacency_list[nodeb].add(nodea)
    
    def is_edge(self, nodea, nodeb):
        # indicates whether or not a pair of nodes are adjacent
        return nodeb in self.adjacency_list[nodea]
    
    def get_neighbors(self, node):
        # gives a set of all nodes adjacent to node n
        return self.adjacency_list[node]
    
    def get_nodes(self):
        # get a set of all the nodes in the graph
        return self.adjacency_list.keys()

