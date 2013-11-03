def IsZeroForcingSet(graph):

	colored_nodes = graph.GetColoredNodes()

	colored_nodes_child_count = 0

	for cnode in colored_nodes:

		children = graph.GetNodeChildren(cnode)

		colored_nodes_child_count += len(children)

		color_count = 0

		for child in children:

			if not graph.IsColored(child):

				color_count += 1

		if color_count == 1:

			graph.SetNodeColor(children[0], 1)

			if len(graph.GetColoredNodes()) == len(graph.GetGraph()):

				return 1

			elif colored_nodes_child_count == 0:

				return 0

			else:

				return IsZeroForcingSet(graph)

	return 0








