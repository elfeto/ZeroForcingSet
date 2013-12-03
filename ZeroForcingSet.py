import itertools

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


