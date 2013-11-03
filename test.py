from graph import Graph
from ZeroForcingSet import *

g = Graph() # create a new graph object

g.AddNode() # add node

g.AddNode() # add node

g.AddNode() # add node

g.AddNode() # add node

g.AddChild(0, 1)

g.AddChild(0, 2)

g.AddChild(1, 3)

g.AddChild(3, 2)

g.AddChild(3, 4)

g.AddChild(2, 4)

g.SetNodeColor(0, 1)# Coloring node 0

g.SetNodeColor(1, 1)# Coloring node 0

print g.GetGraph()# Graph Before ZFS

print IsZeroForcingSet(g)

print g.GetGraph()# Graph After ZFS