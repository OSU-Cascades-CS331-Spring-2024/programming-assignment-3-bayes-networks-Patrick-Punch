from network import BayesNetwork
from node import Node

def main():
    # Create an instance of BayesNetwork
    network = BayesNetwork()

    # Create the nodes
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")

    # Set conditional probability tables for each node
    a_cpt = {
        "a₀" : 0.9, # P(a₀) = 0.9
        "a₁" : 0.1 # P(a₁) = 0.1
    }
    node_a.set_cpt(a_cpt)

    b_cpt = {
        "b₀": {
            ("a₀") : 0.8, # P(b₀ |a₀) = 0.8
            ("a₁") : 0.3  # P(b₀ |a₁) = 0.3
        },
        "b₁" : {
            ("a₀") : 0.2, # P(b₁ |a₀) = 0.2
            ("a₁") : 0.7  # P(b₁ |a₁) = 0.7
        }
    }
    node_b.set_cpt(b_cpt)

    c_cpt = {
        "c₀": {
            ("b₀") : 0.999, # P(c₀ |b₀) = 0.999
            ("b₁") : 0.6    # P(c₀ |b₁) = 0.6
        },
        "c₁" : {
            ("b₀") : 0.001, # P(c₁ |b₀) = 0.001
            ("b₁") : 0.4    # P(c₁ |b₁) = 0.4
        }
    }
    node_c.set_cpt(c_cpt)

    d_cpt = {
        "d₀": {
            ("a₀") : 0.6, # P(d₀ |a₀) = 0.6
            ("a₁") : 0.2  # P(d₀ |a₁) = 0.2
        },
        "d₁" : {
            ("a₀") : 0.4, # P(d₁ |a₀) = 0.4
            ("a₁") : 0.8  # P(d₁ |a₁) = 0.8
        }
    }
    node_d.set_cpt(d_cpt)

    # add parents and children
    node_a.set_children([node_b, node_d])
    node_b.set_children([node_c])
    node_c.set_parents([node_b])
    node_b.set_parents([node_a])
    node_d.set_parents([node_a])

    # add nodes to network
    network.add_node(node_a)
    network.add_node(node_b)
    network.add_node(node_c)
    network.add_node(node_d)

    print("Network before initialization:")
    print(network)
    network.initialize_network()
    print("\nNetwork after initialization:")
    print(network)

    node_b.create_instance((0, 1))
    print(network)


if __name__ == "__main__":
    main()