Patrick Punch
CS 331 Spring 2024
6/6/2024
Collaborators: Kevin, Daniel, Nathan, John

* You can run this implementation by navigating to /programming-assignment-3-bayes-networks-Patrick-Punch, and typing `python3 drug.py` to run the drug file, and `python3 insider.py` into the terminal for the insider file. These files when run will display to the terminal the status of the network before and after initialization, as well as after instantiation of a node.

* If you want to run a different test for this implementation, you'll need to follow these steps:
    1. Instantiate a network object
    2. Create the nodes that you want in the network using `Node("node_name")`
    3. Define and set the conditional probability tables for each node using `node.set_cpt()`
    4. Set the Parents and Children for each node using `node.set_parents()` and `node.set_parents()`
        - both of these functions use a list as the argument, so if you are only adding one child/parent it should be passed as `node.set_children([child])` or `node.set_parents([parent])`
    5. Add the nodes to the network using `network.add(node_object)`
    6. Now, you can view the network you created with `print(network)`
    7. Initialize the network using `network.initialize()`
    8. Lastly, if you want to instantiate a specific node, you can use `node.create_instance(belief)`, where belief is the value you are instantiated, represented as a tuple. 

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/v-9ldGdo)
