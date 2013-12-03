from Graph import Graph
from ZeroForcingSet import *
import pydot


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

cont = 0

for a in comb:
	x = CreateZeroForcingLattice(g, a)
	graph = create_digraph(x)
	print graph
	g = pydot.graph_from_dot_data(graph)
	File = cont.tostring() + "test.png"
	File1  = cont.tostring() + "test.pdf"
	cont = cont + 1
	g.write_png(File)
	g.write_pdf(File1)

