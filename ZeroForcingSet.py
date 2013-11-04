def IsZeroForcingSet(graph):
	
	ischanged = True
		
	while ischanged == True:
			
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
		
	status = True
		
	for node in graph.GetAllNodes():
			
		if not graph.IsColored(node):
				
			status = False
		
	return status
