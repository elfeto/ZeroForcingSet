from Graph import Graph
from ZeroForcingSet import *
import pydot

def create_digraph(x):
	tup = x.pop(0)
	parent = tup[0]
	print parent
	connect = ""
	for tuple in x:
		for conn in tuple[1]:
			if tuple[0][0] in parent:
				connect = connect + '"'+ str(parent)[1:-1] + '" -> "' + str(conn) + '";\n'
			else :
				connect = connect + '"'+ str(tuple[0])[1:-1] + '" -> "' + str(conn) + '";\n'
	dg = 'digraph G {\n' + connect + '}'
	return dg

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

x = list()

for a in comb:
	x.append(CreateZeroForcingLattice(g, a))

for i in x:
	lgraph = create_digraph(i)
	g = pydot.graph_from_dot_data(lgraph)	
	File = str(cont) + "test.png"
	cont = cont + 1
	g.write_png(File)

