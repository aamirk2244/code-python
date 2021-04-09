from graphviz import Digraph

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = self.left = None
 



class BST(TreeNode):
    def __init__(self, value , parent = None):
        super().__init__(value)
        self.parent = parent
        
    def insert(self, value):
        if value  < self.value:
            if self.left is None: self.left = BST(value, self)
            else: self.left.insert(value)
        
        if value > self.value:
            if self.right is None: self.right = BST(value, self)
            else: self.right.insert(value)
    
    def visualize_tree(self):
            if self is None: return 'Nothing in the tree!'
            def add_nodes_edges(self, dot=None):
                # Create Digraph object
                if dot is None:
                    dot = Digraph()
                    dot.attr('node', shape='circle')
                    dot.node(name=str(self), label=str(self.value)) 

                for child in [self.left, self.right]:  # do for all children 
                    if child is not None:
                        if child == self.left: dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')
                        if child == self.right: dot.attr('node', shape='doublecircle', style='filled', fillcolor='seashell')
                        dot.node(name=str(child) ,label=str(child.value))
                        dot.edge(str(self), str(child))
                        dot = add_nodes_edges(child, dot=dot)  # recursive call 

                return dot

            # Add nodes recursively and create a list of edges
            dot = add_nodes_edges(self)

            # Visualize the graph
            display(dot)

b = BST(100)
b.insert(150)
b.insert(10)
b.insert(15)
b.insert(1)
b.insert(250)
b.insert(101)
b.insert(151)
b.insert(18)
b.visualize_tree()

