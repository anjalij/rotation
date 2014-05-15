#this program should tie together all of the trees and all of the nodes. 
class Tree:
    def __init__(self,name=[], nodes=0):
        self.name=[]
        self.nodes=0
        self.string=0
        
    def __rep__(self):
        print str(self.name)+":"+str(self.nodes)

class Node:
    def __init__(self, name=1, color='black',left="leaf",right="leaf"):
        self.right=right
        self.left=left
        self.name=name
        self.color=color
    
class Leaf(Node):
    def __init__(self):
        self.name = 0
        self.left=None
        self.right=None
        
def all_trees_le_n_nodes(n):
    zero_tree=Tree() 
    print zero_tree.nodes
    zero_tree.name=[Leaf()] #cannot make the leaf the "self" because otherwise I will be defining trees as concatenations of other trees. 
    all_trees=[zero_tree]
    all_trees_string=[zero_tree.string]
    i=0
    while i<n:
        for element1 in all_trees:
             if element1.nodes<=i: # did this otherwise the program wastes time trying to run calculate g.nodes+f.nodes with the new elements
                for element2 in all_trees:
                    #color_counter=color_counter+1                   
                    if element2.nodes<=i:
                        if element1.nodes+element2.nodes==i: #not sure about the indexing
                            tree=element1.name+element2.name                           
                            new_node=Node()
                            new_node.left=element1.name[-1] #this is because the element themselves are lists of nodes, and we just want to link the last node as the left/right children. When we append the new node it adds to the last position in the list
                            new_node.right=element2.name[-1]
                            tree.append(new_node) #this should mean that the "Self" of a member of class Tree() is a list of nodes
                            current_tree=Tree() #can i define a self as a collections of members of another class?!
                            current_tree.name=tree
                            current_tree.string=[element1.string, element2.string]
                            current_tree.nodes=i+1
                            if current_tree not in all_trees:
                                all_trees.append(current_tree)
                                all_trees_string.append(current_tree.string)
        i=i+1
    return  all_trees_string, len(all_trees) #,all_trees, len(all_trees)
print all_trees_le_n_nodes(3)

#prints all trees exactly equal to n nodes
#Catalan Numbers
def all_trees_n_nodes(n):
    zero_tree=Tree() 
    print zero_tree.nodes
    zero_tree.name=[Leaf()] #cannot make the leaf the "self" because otherwise I will be defining trees as concatenations of other trees. 
    all_trees=[zero_tree]
    all_trees_string=[zero_tree.string]
    all_trees_n_nodes=[]
    all_trees_n_nodes_string=[]
    i=0
    while i<n:
        for element1 in all_trees:
             if element1.nodes<=i: # did this otherwise the program wastes time trying to run calculate g.nodes+f.nodes with the new elements
                for element2 in all_trees:
                    #color_counter=color_counter+1                   
                    if element2.nodes<=i:
                        if element1.nodes+element2.nodes==i: #not sure about the indexing
                            tree=element1.name+element2.name                           
                            new_node=Node()
                            new_node.left=element1.name[-1] #this is because the element themselves are lists of nodes, and we just want to link the last node as the left/right children. When we append the new node it adds to the last position in the list
                            new_node.right=element2.name[-1]
                            tree.append(new_node) #this should mean that the "name" of a member of class Tree() is a list of nodes
                            current_tree=Tree() #can i define a self as a collections of members of another class?!
                            current_tree.name=tree
                            current_tree.string=[element1.string, element2.string]
                            current_tree.nodes=i+1
                            if current_tree not in all_trees:
                                all_trees.append(current_tree) # this is just a collection of trees
                                all_trees_string.append(current_tree.string) # this is the string of parentheses
        i=i+1
        for element in all_trees:
            if element.nodes==n:
                all_trees_n_nodes.append(element) # this is just a collection of trees
                all_trees_n_nodes_string.append(element.string) # this is the string of parentheses
    return all_trees_n_nodes_string, len(all_trees_n_nodes_string) # all_trees_n_nodes, len(all_trees),
print all_trees_n_nodes(3)

