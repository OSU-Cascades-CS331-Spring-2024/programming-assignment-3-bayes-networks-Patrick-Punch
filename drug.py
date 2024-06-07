from network import BayesNetwork
from node import Node

def main():
    # Create an instance of BayesNetwork
    network = BayesNetwork()

    # Add nodes
    drug_node = Node("Drug")

    cure_node = Node("Cure")

    # Set conditional probability tables for each node
    drug_cpt = {
        "d₀" : 0.9, # P(d₀) = 0.9
        "d₁" : 0.1 # P(d₁) = 0.1
    }
    drug_node.set_cpt(drug_cpt)

    cure_cpt = {
        "c₀": {
            ("d₀") : 0.5, # P(c₀ |d₀) = 0.5
            ("d₁") : 0.25 # P(c₀ |d₁) = 0.25
        },
        "c₁" : {
            ("d₀") : 0.5, # P(c₁ |d₀) = 0.5
            ("d₁") : 0.75 # P(c₁ |d₁) = 0.75
        }
    }
    cure_node.set_cpt(cure_cpt)
    drug_node.set_children([cure_node])
    cure_node.set_parents([drug_node])

    # Add nodes to the network
    network.add_node(drug_node)
    network.add_node(cure_node)

    # Print the network before initialization, after initialization, and after instantiation
    print("Network before initialization:")
    print(network)
    network.initialize_network()

    print("\nNetwork after initialization:")
    print("\n")
    print(network)

    cure_node.create_instance((0, 1))
    print("\nProbability that the patient was part of the drug study given that they have been cured:", drug_node.belief[1])

if __name__ == "__main__":
    main()