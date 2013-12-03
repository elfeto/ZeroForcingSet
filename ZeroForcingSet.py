import itertools
from Graph import Graph

def IsZeroForcingSet(graph):
	
	ischanged = True
		
	while ischanged:
			
		ischanged = False
		
		colored_nodes = graph.GetColoredNodes()

		for cnode in colored_nodes:
					
			count = 0
					
			next_colored_node = None

			children = graph.GetNodeChildren(cnode)
					
			for child in children:
						
				if not graph.IsColored(child):
							
						count = count + 1
					
						next_colored_node = child
				
			if count == 1:
					
				graph.SetNodeColor(next_colored_node, 1)
						
				ischanged = True
		
	for node in graph.GetAllNodes():
			
		if not graph.IsColored(node):
				
			return False
		
	return True

def ZeroForcingNumber(graph):

	gra = list()

	for i in range(graph.GetGraphSize()):
		
		gra.append([list(x) for x in itertools.combinations(range(graph.GetGraphSize()),i)])

	for h in gra:
	
		for k in h:
			
			for j in k:
				
				graph.SetNodeColor(j, 1)

			if IsZeroForcingSet(graph):
	
				return len(k)

			for l in graph.GetAllNodes():

				graph.SetNodeColor(l, 0)

def ZeroForcingLattice(graph, zero_forcing_number):

	gra = list()

	combinations = list()

	for i in range(graph.GetGraphSize()):
		
		gra.append([list(x) for x in itertools.combinations(range(graph.GetGraphSize()),i)])

	for m in graph.GetAllNodes():
		
		graph.SetNodeColor(m, 0)

	for h in gra:
		
		for k in h:

			for j in k:

				graph.SetNodeColor(j, 1)

			if IsZeroForcingSet(graph) and len(k) == zero_forcing_number:

				combinations.append(k)		

			for l in graph.GetAllNodes():

				graph.SetNodeColor(l, 0)

	return combinations


def CreateZeroForcingLattice(graph, lattice_nodes):

	for l in graph.GetAllNodes():

		graph.SetNodeColor(l, 0)

	Parents = None

	Sons = list()

	List = list()

	Sons2 = list()

	Final = list()

	Knode = None

	childrens = list()

	for combination in lattice_nodes:

		graph.SetNodeColor(combination, 1)

	Parents = lattice_nodes

	color = graph.GetColoredNodes()

	for cnode in color:

		childrens.append(graph.GetNodeChildren(cnode))

	for num in Parents:
		count = 0
		for child in childrens:

			if child in graph.GetNodeChildren(num) and not graph.IsColored(child):
								
				count = count + 1

		if count == 1:

			Sons.append(child)

	for i in Sons:
		graph.SetNodeColor(i, 1)

	List.append(Parents)
	List.append(Sons)
	Final.append(List)

	ischanged = True

	while ischanged:
			
		ischanged = False
		
		colored_nodes = graph.GetColoredNodes()
		
		next_colored_node = list()
		
		Sons1 = list()	

		for cnode in colored_nodes:
		
			List1 = list()
			count = 0
					
			next_cnode = None

			children = graph.GetNodeChildren(cnode)
					
			for child in children:
						
				if not graph.IsColored(child):
							
						count = count + 1
					
						next_cnode = child

						Parents = cnode

			if count == 1:

				List1.append([Parents])
				List1.append([next_cnode])
				Sons1.append(next_cnode)
				Final.append(List1)
										
				ischanged = True

		for i in Sons1:
			graph.SetNodeColor(i, 1)		

	return Final
