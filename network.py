class BayesNetwork:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        self.nodes[node.name] = node

    def initialize_network(self):
        print("--- Initializing Network ---")
        for _, node in self.nodes.items():
            node.initialize()

    def __str__(self):
        network = "\n\t\t\tNodes: \n"
        network += "\n".join([str(node) for node in self.nodes.values()])
        return network