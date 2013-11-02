from graph import Graph

g = Graph() # create a new graph object

g.AddNode() # add node

g.AddNode() # add node

for node in g.GetAllNodes(): # iterate over the list of nodes

	if node != 0: # if node is not node 0

		g.AddChild(0, node) # add node as a child of 0

print g.GetGraph() # Graph Before coloring node 0

g.SetNodeColor(0, 1)# Coloring node 0

print g.GetGraph()# Graph after coloring node 0