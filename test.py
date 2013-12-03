from Graph import Graph
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

comb = ZeroForcingLattice(g, ZeroForcingNumber(g))

for a in comb:
	CreateZeroForcingLattice(g, a)
