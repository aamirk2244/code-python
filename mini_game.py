import os
import random
from graphviz import Digraph
os.system("")
class style():
    RED = '\033[31m'
    GREEN = '\033[32m'
    CBOLD     = '\33[1m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'
   
def Print(table, r = None, c = None):
    ROWS = COLUMNS = 5
    for row in range(ROWS):
            for column in range(COLUMNS):
                if table[row][column] == 'G': print(  style.CBOLD + style.RED  +   table[row][column], end = '| ')
                elif r == row and c == column: print(style.CBOLD + style.GREEN + str(table[row][column]), end = '| ')
                else: print( style.RESET + str(table[row][column]), end = '| ')
            print()
    
def creating_table_and_fixing_initial_state(table, ROWS, COLUMNS, goal_state_index ):
    Print(table)
    
    print('Enter your Initial State, row or column should not be negative, It can be start from 0')
    r = input('row = ')
    c = input('column = ')
    if r + c == goal_state_index: raise ValueError('You are already on the Goal Sate ')
    if int(r) > ROWS-1 or int(r) < 0 or int(c) > COLUMNS-1 or int(c) < 0 or len(r) > 2 or len(c) > 2 :raise IndexError('rows or column Indexes are Invalid')
    r = int(r)
    c = int(c)
    if table[r][c] == 'G':return 'You choose Goal state box'
    
    Print(table, r,c)
    initial_state = str(r) + str(c)
    return initial_state

# RULE OF THE GAME is , cannot skip any neghbour box, go from one box to other

class node:
    def __init__(self, value, parent):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None
        self.top = None
        self.down = None
class Tree:
    def __init__(self, table, Rows, Column):
        self.root = None
        self.rows = Rows
        self.columns = Column
        self.initial_state = None
        self.table = None
        self.goal_state_index = ''
        self.goal_value = 'G'
        self.path_made = {}
        self.saved_path_to_goal = []
        self.total_cost_towards_goal_state = 0
        self.already_traverse_states = {}
        for row in range(self.rows):
            for column in range(self.columns):
                self.already_traverse_states[str(row) + str(column)] = False
                self.path_made[str(row) + str(column)] = False
                
    def getRoot(self):return self.root
    def set_table_path_toward_goal_state(self, table, ROWS, COLUMN, initial_state):
        self.initial_state = initial_state
        self.parent = False
        self.rows = ROWS
        self.columns = COLUMN
        self.table = table
        self.root = node(initial_state, None)       # root will be the inital state
        q = [self.root]           # making our path from initial state to the goal state
        temp = None
        length = 5
        row_index = column_index = 0
        while q:
            temp = q.pop(0)
             
            if table[int(temp.value[0])][int(temp.value[1])] == self.goal_value: self.goal_state_index = temp.value   # saving goal state index of the grid
            row_index = int(temp.value[0])
            column_index = int(temp.value[1])
            if temp.value == initial_state: self.initial_state = temp          # initial_state will be pointing to initial position of agent
            if row_index + 1 < ROWS and self.path_made[temp.value] is False:
                temp.down = node(str(row_index + 1) + str(column_index), temp)  # it means that path exists on down side
                if temp.value == self.goal_state_index: return self.Save_the_path(temp)    # if goal state found don't make further environment
                q.append(temp.down)

            if column_index + 1 <  COLUMN and self.path_made[temp.value] is False:
                temp.right = node(str(row_index) + str(column_index+1), temp) # it means that path exists on right side
                if temp.value == self.goal_state_index: return self.Save_the_path(temp)    # if goal state found don't make further environment
                q.append(temp.right)
            if row_index - 1 >= 0 and self.path_made[temp.value] is False:
                temp.top = node(str(row_index-1) + str(column_index), temp)      # it means that path exists on top side
                if temp.value == self.goal_state_index: return self.Save_the_path(temp)    # if goal state found don't make further environment
                q.append(temp.top)
            if column_index - 1 >= 0 and self.path_made[temp.value] is False:
                temp.left = node(str(row_index) + str(column_index-1), temp)   # it means that path exists on left side
                if temp.value == self.goal_state_index: return self.Save_the_path(temp)    # if goal state found don't make further environment
                q.append(temp.left)
            

            self.path_made[temp.value] = True
            
    def Save_the_path(self, goal_state_founded):
        # goal state founded now moving to root of this goal to save the path
        
        path = [goal_state_founded]
        while goal_state_founded.parent is not None:
            
            path.append(goal_state_founded.parent)
            self.total_cost_towards_goal_state += self.table[int(goal_state_founded.parent.value[0])][int(goal_state_founded.parent.value[1])]
            goal_state_founded = goal_state_founded.parent
        print('Path length is --------->', len(path))
        path.reverse()    # path is saved here
        self.saved_path_to_goal = path
        path_indexes = []
        for index in path:
            path_indexes.append(index.value)
            print('index of path traversal -->> ', index.value)
        print('Successfully reached    -->>  GOAL ACHIEVED')
        print('Total cost suffered     -->>  ', self.total_cost_towards_goal_state)
        self.display_path_to_resultant_goal(path_indexes)
        return

        
            
                
            
#         already_traversed_states[self.initial_state.value] = True              # initial_state value consist of index of that state
        
    def display_path_to_resultant_goal(self, path):
        print('***********************************************')
        ROWS = self.rows
        COLUMNS = self.columns
        execute = True
        for row in range(ROWS):
                for column in range(COLUMNS):
                    path_index = str(row) + str(column)
                    if path_index in path:
                        if path_index ==  self.initial_state.value:print(style.CBOLD + style.GREEN + str(table[row][column]), end = '| ')
                        elif self.table[row][column] == 'G': print(  style.CBOLD + style.RED  +   table[row][column], end = '| ')
                        else : print(style.CBOLD + style.YELLOW + str(table[row][column]), end = '| ')
                        path.remove(path_index)
                    else:print( style.RESET + str(table[row][column]), end = '| ')
                print()

        print('***********************************************')
        
    def visualize_tree(self, tree):
        found_path =self.saved_path_to_goal[-1]           # this is the goal state node
        if self.root is None: return 'Nothing in the tree!'

        def add_nodes_edges(tree, dot=None):
            # Create Digraph object
            if dot is None:
                dot = Digraph()
                dot.attr('node', shape='circle')
                dot.node(name=str(tree), label=str(tree.value)) 

            for child in [tree.left, tree.right, tree.top, tree.down]:  # do for all children 
                if child is not None:

                    if child == tree.left and child == found_path: dot.attr('node', shape='circle', style='filled', fillcolor='red',size ="0,0")
                    elif child == tree.left : dot.attr('node', shape='circle', style='filled', fillcolor='lightblue',size ="0,0")

                    if child == tree.right and child == found_path: dot.attr('node', shape='doublecircle', style='filled', fillcolor='red',size ="0,0")
                    elif child == tree.right: dot.attr('node', shape='doublecircle', style='filled', fillcolor='seashell',size ="0,0")

                    if child == tree.top and child == found_path: dot.attr('node', shape='circle', style = 'filled', fillcolor = 'red',size ="0,0")
                    elif child == tree.top : dot.attr('node', shape='circle', style = 'filled', fillcolor = 'green',size ="0,0")
                    if child == tree.down and child == found_path: dot.attr('node', shape='doublecircle', style='filled', fillcolor='red',size ="0,0")
                    elif child == tree.down: dot.attr('node', shape='doublecircle', style='filled', fillcolor='yellow',size ="0,0")
                    dot.node(name=str(child) ,label=str(child.value))
                    dot.edge(str(tree), str(child))
                    dot = add_nodes_edges(child, dot=dot)  # recursive call 

            return dot

        # Add nodes recursively and create a list of edges
        dot = add_nodes_edges(tree)


        # Visualize the graph
        display(dot)


            
table = [[3,4,1,3,1],
         [3,3,3,'G',2],
         [3,1,2,2,3],
         [4,2,3,3,3],
         [4,1,4,3,2]]
rows = columns = 5
goal_state_index = '13'
initial_state = creating_table_and_fixing_initial_state(table, rows, columns, goal_state_index)
b = Tree(table, rows, columns)
b.set_table_path_toward_goal_state(table,rows, columns, initial_state)
root = b.getRoot()
print('Note:  Yellow colour in 2d array -->> is the path followed')
print('Note:  Green colour  in 2d array -->> is the Initial state')
print('Note:  Red colour in 2d array   -->> is the Goal state')

b.visualize_tree(root)





    
