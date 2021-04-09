import networkx as nx
import matplotlib.pyplot as plt

%matplotlib inline
import warnings
warnings.filterwarnings("ignore")
def draw_graph_with_nx(G):
    pos = nx.spring_layout(G, k=1000, iterations=200)  #k is for spacing between nodes
    options = {'node_color':'pink', 'alpha':1, 'node_size':2500, 'width':0.2, 'font_color':'darkred', 
               'font_size':12, 'arrows':True, 'edge_color':'brown', 
               'arrowstyle':'Fancy, head_length=1, head_width=1, tail_width=.4'
              }
    weight_labels = nx.get_edge_attributes(G, 'weight')
    labels = nx.get_node_attributes(G, 'label')
    nx.draw(G, pos, labels=labels, **options)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weight_labels, font_size=10)
    plt.show()

    
class Graphs:
    def __init__(self):
        self.g = {} 
    
    def addNode(self, node):
        if node in self.g:return
        self.g[node] = []
    def addEdge(self, src, dest, cost):
        if src not in self.g: raise ValueError('Source is not present in Graph')
        if dest not in self.g: raise ValueError('Destination not present in Graph')
        destinations = self.g[src]
        destination_and_cost = (dest,cost)
        replace = 0
        for DEST,COST in destinations:       # destination is tuple which contain the destination and cost
            replace += 1                     # knowing the index of the tuple
            if DEST == dest: 
                destinations[replace] = destination_and_cost   # if same destination across that source found then repace it with the new one 
                return
        destinations.append(destination_and_cost)     #  append the new destination
  
    
    def dijkstra(self, src, dest):
        to_visit = list(self.g.keys()) # these nodes will be visited
        inf = float('inf')
        distances = {node:inf for node in to_visit}
        distances[src] = 0
        current = src              # current will contain the minimum neghbour
        best_path = {}
        best_path[(src, src)] = [src]   # path from source to source is also a source
        
        while to_visit:
            current = min(to_visit, key=lambda node:distances[node])  # mapping key with value in dists for min
            neighbours = self.g[current]
            un_visited = []
            if distances[current] == inf: break
            for node,cost in neighbours:
                if node in to_visit:
                    un_visited.append((node,cost))
            for node, cost in un_visited:
                old_cost = distances[node]           # this is infinity or already calculated cost
                new_cost = distances[current] + cost        # this should be less
                
                if new_cost < old_cost:
                    path_to_current = best_path[(src, current)][:]
                    best_path[(src, node)] = path_to_current
                    best_path[(src, node)].append(node)
                    distances[node] = new_cost           # update that infinity or already calculated cost 
                    
            to_visit.remove(current)
#             print(distances)
        
        ######################## the below area is not included in the algorithm
        show_minimum_cost_graph(distances, best_path[(src,dest)], self.g)
        show_best_path(best_path[(src, dest)], distances)
        return best_path[(src, dest)],  distances[dest]

      
    def draw_graph(self):
        G = nx.DiGraph()
        for src in self.g:
            G.add_node(src, label=src)
            for dest in self.g[src]:
                G.add_edge(src, dest[0], weight=str(dest[1]))

        draw_graph_with_nx(G)   


    def traverse_graph(self, start):
        q = [start]
        visited = []
        
        while q:
            current = q.pop(0)
            
            if current in visited:
                continue
                
            print(current)
            
            visited.append(current)
            
            next_nodes = self.g[current]
            
            for n in next_nodes:
                q.append(n[0])
                

def show_best_path( best_path, distances):
    # best_path = ['A' , 'B', 'D']        example
    print("***************** All Shortest Paths from source *****************")
    g = Graphs()
    for nodes in best_path: g.addNode(nodes)
    ist_time=  True
    for nodes in best_path:
        if ist_time : 
            src = nodes
            ist_time = False
            continue
        
        g.addEdge(src, nodes, distances[nodes])
    g.draw_graph()

    
def show_minimum_cost_graph(distances,best_path, main_graph ):
        
        print('******************Minimum Cost Graph from ' + best_path[0] + ' to ' + best_path[-1] + '**********************')
        g = Graphs()
        for nodes in best_path: g.addNode(nodes)
        length = len(best_path)
        for nodes in range(length):
            if nodes + 1 < length:
                source = best_path[nodes]
                destination = best_path[nodes + 1]
                for dest,this_cost in main_graph[source]:
                    if dest == destination: cost = this_cost 
                g.addEdge(source,destination, cost)
        print('best path is ', best_path)
        g.draw_graph()
        
    
    
g = Graphs()
nodes = ['A', 'B', 'C', 'D', 'G', 'S']
edges = [('A', 'B', 3),
         ('A', 'C', 1), 
         ('B', 'D', 3),
         ('C', 'D', 1),
         ('C', 'G', 2),
         ('D', 'G', 3), 
         ('S', 'A', 1),
         ('S', 'G', 12)
        
        ]
for i in nodes:
    g.addNode(i)
for e in edges:
    g.addEdge(e[0], e[1], e[2])

g.draw_graph()
print(g.dijkstra('S','G'))
    
    ##################
         
         # nodes = ['S', 'A', 'B', 'C', 'D', 'E', 'F', 'G1', 'G2', 'G3']
# edges = [('A', 'G1', 9),
#          ('A', 'B', 3), 
#          ('S', 'D', 6),
#          ('S', 'A', 5),
#          ('S', 'B', 9), 
#          ('B', 'A', 2),
#          ('B', 'C', 1),
#          ('C', 'S', 6),
#          ('C', 'G2', 5),
#          ('C', 'F', 7),
#          ('D', 'C', 2),
#          ('D', 'E', 2),
#          ('D', 'S', 6),
#          ('E', 'G3',7),
#          ('F', 'D', 2),
#          ('F', 'G3', 8)]

