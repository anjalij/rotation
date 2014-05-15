#so this program does get all trees without recursion.
#one program gives all the trees less than equal to n nodes, and one program gives all nodes exactly equal to n nodes...prints them, but all programs populate the class Tree with all trees less than equal to n nodes.
#the next step would be to link this class Tree with the class nodes.

class Tree:
    def __initi__(self,name=[], nodes=0):
        self.name=[]
        self.nodes=0
        
    def __rep__(self):
        print str(self.name)+":"+str(self.nodes)

#prints all trees less than ewual to n.
def all_trees_less_than_n(n):
    zero_nodes=Tree()
    zero_nodes.name=0
    zero_nodes.nodes=0
    all_trees=[zero_nodes]
    all_trees_names=[zero_nodes.name]
    i=0
    while i<n: # less than because a loop adds another node and we dont want to add any more after n.
        #print "I:" +str(i)
        for g in all_trees:
            if g.nodes<=i: # did this otherwise the program wastes time trying to run calculate g.nodes+f.nodes with the new elements
                #print "g: " +str(g.name)
                for f in all_trees:
                    if f.nodes<=i: # same as above...there should be a better way of preventing these extra calculations.
                        #print "f: "+str(f.name)
                        if g.nodes+f.nodes==i:
                            #print "yes"
                            current_tree=Tree()
                            current_tree.name=[f.name,g.name]
                            #print "current tree:" +str(current_tree.name)
                            current_tree.nodes=i+1   
                            #if current_tree not in all_trees: # do I need this?
                            all_trees.append(current_tree)
                            all_trees_names.append(current_tree.name)
                            #print "all trees: " +str(all_trees_names)
        i=i+1
    return all_trees_names, len(all_trees_names)
print all_trees_less_than_n(3)

#prints all trees exactly equal to n nodes
#Catalan numbers
def all_trees_n_nodes(n):
    zero_nodes=Tree()
    zero_nodes.name=0
    zero_nodes.nodes=0
    all_trees=[zero_nodes]
    all_trees_names=[zero_nodes.name]
    all_trees_length_n=[]
    i=0
    while i<n: # less than because a loop adds another node and we dont want to add any more after n.
        #print "I:" +str(i)
        for g in all_trees:
            if g.nodes<=i: # did this otherwise the program wastes time trying to run calculate g.nodes+f.nodes with the new elements
                #print "g: " +str(g.name)
                for f in all_trees:
                    if f.nodes<=i: # same as above...there should be a better way of preventing these extra calculations.
                        #print "f: "+str(f.name)
                        if g.nodes+f.nodes==i:
                            #print "yes"
                            current_tree=Tree()
                            current_tree.name=[f.name,g.name]
                            #print "current tree:" +str(current_tree.name)
                            current_tree.nodes=i+1   
                            #if current_tree not in all_trees: #do I need this
                            all_trees.append(current_tree)
                            all_trees_names.append(current_tree.name)
                            #print "all trees: " +str(all_trees_names)
        i=i+1
        for g in all_trees:
            if g.nodes==n:
                all_trees_length_n.append(g.name)
    return all_trees_length_n, len(all_trees_length_n)
print all_trees_n_nodes(5)
