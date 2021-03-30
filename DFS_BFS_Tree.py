# This code runs outside the AI-env 
from graphviz import Digraph
class node:
    def __init__(self, value, parent = None):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
class BST:
    def __init__(self):
        self.root = None
        self.parent = None
    def getRoot(self):return self.root
    def insert(self, value, current):
        if self.root is None:
            self.root = node(value, None)
            return
        if value < current.value:
            if current.left is not None:self.insert(value, current.left)
            else:
                current.left = node(value, current)
                
        if value > current.value:
            if current.right is not None:self.insert(value, current.right)
            else:
                current.right = node(value, current)

    def Inorder(self, current):
        
        if(current is None):
            return
        print(current.value)
        self.Inorder(current.left)
        
        self.Inorder(current.right)
    def BFS(self, value):
        print('In BFS')
        q = [self.root]
        while q:
            
            current = q.pop(0)
            if current is not None and current.value == value:return True
            if current is not None:
                q.append(current.left)
                q.append(current.right)
        print('value not found')
        return False
    def DFS(self, value):
        print("IN DFS")
        stack = [self.root]
        while stack:
            
            current = stack.pop(-1)  # it will get last element
            if current is not None and current.value == value:return True
            if current is not None:
                stack.append(current.right)
                stack.append(current.left)
        print('value not found')
        return False
            
            
    def visualize_tree(self, tree):
            if self.root is None: return 'Nothing in the tree!'
            def add_nodes_edges(tree, dot=None):
                # Create Digraph object
                if dot is None:
                    dot = Digraph()
                    dot.attr('node', shape='circle')
                    dot.node(name=str(tree), label=str(tree.value)) 

                for child in [tree.left, tree.right]:  # do for all children 
                    if child is not None:
                        if child == tree.left: dot.attr('node', shape='circle', style='filled', fillcolor='lightblue')
                        if child == tree.right: dot.attr('node', shape='doublecircle', style='filled', fillcolor='seashell')
                        dot.node(name=str(child) ,label=str(child.value))
                        dot.edge(str(tree), str(child))
                        dot = add_nodes_edges(child, dot=dot)  # recursive call 

                return dot

            # Add nodes recursively and create a list of edges
            dot = add_nodes_edges(tree)

            # Visualize the graph
            display(dot)

b = BST()
b.insert(50, None)
root = b.getRoot()
b.insert(30, root)
b.insert(30, root)
b.insert(15, root)
b.insert(35, root)
b.insert(7, root)
b.insert(22, root)
b.insert(31, root)
b.insert(40, root)

#########
b.insert(70, root)
b.insert(62, root)
b.insert(68, root)
b.insert(54, root)

b.insert(87, root)
b.insert(100, root)
b.insert(85, root)

b.insert(62, root)
b.visualize_tree(root)
print(b.BFS(100))
print(b.DFS(100))
    
