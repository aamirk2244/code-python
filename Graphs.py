import networkx as nx
import matplotlib.pyplot as plt
%matplotlib inline
import warnings
warnings.filterwarnings("ignore")
def draw_graph_with_nx(G):
    pos = nx.spring_layout(G, iterations = 200)
    options = {'node_color': 'white', 'alpha': 1, 'node_size': 2000, 'width': 0.002, 'font_color': 'darkred', 'font_size': 25, 'arrows': True, 'edge_color': 'brown', 'arrowstyle': 'Fancy, head_length = 1, head_width = 1, tail_width = .4'}
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, labels = labels, **options)
    plt.show()
class Graphs:
    def __init__(self):
        self.g = {} 
    
    def addNode(self, node):
        if node in self.g:return
        self.g[node] = []
    def addEdge(self, src, dest):
        if src not in self.g: raise ValueError('Source is not present in Graph')
        if dest not in self.g: raise ValueError('Destination not present in Graph')
        destinations = self.g[src]
        if dest in destinations:return
        self.g[src].append(dest)
    
    def draw_graph(self):
        G = nx.DiGraph()
        for src in self.g:
            G.add_node(src, label = src)
            for dest in self.g[src]:
                G.add_edge(src, dest)
        draw_graph_with_nx(G)
        
g = Graphs()
nodes = ['a', 'd', 'b', 'l', 'k']
edges = [('a', 'd'), ('d', 'b'), ('b', 'l'), ('k', 'd'), ('a', 'b'), ('b', 'a')]
for i in nodes:
    g.addNode(i)
for e in edges:
    g.addEdge(e[0], e[1])
g.draw_graph()
    
