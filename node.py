class Node:
    def __init__(self, name, parents=None, cpt=None):
        self.name = name
        self.parents = []
        self.children = []
        self.cpt = cpt
        self.λ_msg = (1,1)
        self.λ_val = (1,1)
        self.π_val = (0,0)
        self.π_msg = [1,1]
        self.belief = None
        self.is_instantiated = False

    def set_cpt(self, cpt):
        self.cpt = cpt

    def set_children(self, children):
        for child in children:
            self.children.append(child)
    
    def get_children(self):
        for child in self.children:
            return child.name

    def set_parents(self, parents):
        for parent in parents:
            self.parents.append(parent)

    def get_parents(self):
        for parent in self.parents:
            return parent.name

    def probability_given_parents(self, evidence):
        parent_values = tuple([evidence[parent] for parent in self.parents])
        if parent_values in self.cpt:
            return self.cpt[parent_values][self.name]
        else:
            return 1

    def __str__(self):
        node = f"\n{self.name} Node:, Parents: {self.get_parents()}, Children: {self.get_children()}, \nCPT: {self.cpt}, Belief: {self.belief}, \nλ-Message: {self.λ_msg}, λ-values: {self.λ_val}, \nπ_messages : {self.π_msg}, π-values: {self.π_val}"
        return node


    def initialize(self):
        '''
        Initialization Steps:
            1. set λ-values and λ-msgs to 1
            2. A has m values for 1 ≤ j ≤ m
                set P'(aⱼ) = p(aⱼ), and
                set π(aⱼ) = p(aⱼ)
            3. ∀ B ∈ S(A), compute π-message for B
            4. ∀ B ∈ S(A), post a new π-message to B using update rule C
        '''
        print(f"~~~ Initializing Node: {self.name} ~~~")

        if len(self.parents) > 0:
            for parent in self.parents:
                parent.get_belief()
                parent.π_message()
            # compute pi message
            if len(self.children) > 0:
                self.π_message()
        else:
            self.belief = tuple(self.cpt.values())
            # set pi values
            self.π_value(self.π_msg)
            #compute pi message
            if len(self.children) > 0:
                for child in self.children:
                    self.π_message()

    def π_message(self): # goes down
        '''         { 1         if A is instantiated for aⱼ 
        π⁽ᴮ⁾(aⱼ) =  { 0         if A is instantiated but not for aⱼ
                    { P'(aⱼ)/λ⁽ᴮ⁾(aⱼ) if A is not instantiated    
        '''
        new_π_msg = [0, 0]
        for child in self.children:
            for i in range(len(self.belief)):
                new_π_msg[i] = self.belief[i]/child.λ_msg[i]
            self.π_msg = new_π_msg
            self.send_π_message(new_π_msg)

    def send_π_message(self, π_msg):
        if len(self.children) > 0:
            for child in self.children:
                if child.is_instantiated == False:
                    child.π_value(π_msg)
                    child.get_belief()
                    child.π_message()

    def π_value(self, π_msg): 
        '''      ₘ 
        π(bᵢ) =  ∑ P(bᵢ|aⱼ)πᴮ(aⱼ)
                ʲ⁼¹     
        '''
        if self.is_instantiated:
            self.π_val = [0,1]
        prob_of_self = self.cpt.values()
        self.belief = tuple(prob_of_self)
        self.π_val = [tuple(prob_of_self)[0],tuple(prob_of_self)[1]]
        if len(self.parents) > 0:
            # compute pi value
            # P(b₀|a₀) -> child false given parent false
            b0_given_a0 = tuple(tuple(self.cpt.values())[0].values())[0]
            # P(b₀|a₁) -> child false given parent true
            b0_given_a1 = tuple(tuple(self.cpt.values())[0].values())[1]
            # P(b₁|a₀) -> child true given parent false
            b1_given_a0 = tuple(tuple(self.cpt.values())[1].values())[0]
            # P(b₁|a₁) -> child true given parent true
            b1_given_a1 = tuple(tuple(self.cpt.values())[1].values())[1]

            self.π_val[0] = b0_given_a0 * π_msg[0] + b0_given_a1 * π_msg[1]
            self.π_val[1] = b1_given_a0 * π_msg[0] + b1_given_a1 * π_msg[1]

    def λ_message(self): # goes up 
        '''          ₖ    
            λᴮ(aⱼ) = ∑ P(bᵢ|aⱼ)λ(bᵢ)
                    ⁱ⁼¹             
        '''
        if len(self.parents) > 0:
            # compute lambda message
            # P(b₀|a₀) -> child false given parent false
            b0_given_a0 = tuple(tuple(self.cpt.values())[0].values())[0]
            # P(b₀|a₁) -> child false given parent true
            b0_given_a1 = tuple(tuple(self.cpt.values())[0].values())[1]
            # P(b₁|a₀) -> child true given parent false
            b1_given_a0 = tuple(tuple(self.cpt.values())[1].values())[0]
            # P(b₁|a₁) -> child true given parent true
            b1_given_a1 = tuple(tuple(self.cpt.values())[1].values())[1]

            λ_msg_0 = b0_given_a0 * self.λ_val[0] + b1_given_a0 * self.λ_val[1]
            λ_msg_1 = b0_given_a1 * self.λ_val[0] + b1_given_a1 * self.λ_val[1]
            self.λ_msg = [λ_msg_0, λ_msg_1]
            self.send_λ_message(self.λ_msg)

    def send_λ_message(self, λ_msg):
        if len(self.parents) > 0:
            for parent in self.parents:
                parent.λ_msg = λ_msg

    def λ_value(self):
        '''     { 1             if B is instantiated for bᵢ 
        λ(bᵢ) = { 0             if B is instantiated but not for bᵢ
                { πᶜ∈ˢ⁽ᴮ⁾λ⁽ᶜ⁾(bᵢ) otherwise          
        '''
        for parent in self.parents:
            parent.λ_val = self.λ_msg            

    def get_belief(self):
        '''     α is a constant that normalizes P'(B):   ₖ
        P'(bᵢ) = αλ(bᵢ)π(bᵢ)                             ∑ P'(bᵢ) = 1
                                                        ⁱ⁼⁰
        '''
        sum = self.λ_val[0] * self.π_val[0] + self.λ_val[1] * self.π_val[1]
        α = 1 / sum
        self.belief = (float("%.3f" % round(α * self.λ_val[0] * self.π_val[0], 3)),float("%.3f" % round(α * self.λ_val[1] * self.π_val[1], 3)))
        return self.belief

    def create_instance(self, belief):
        print(f"Node {self.name} is being instantiated.")
        self.is_instantiated = True
        self.belief = belief
        self.λ_val = [self.belief[0], self.belief[1]]
        self.λ_message()
        self.λ_value()
        for parent in self.parents:
            parent.get_belief()
            parent.π_message()
        for child in self.children:
            self.π_message()