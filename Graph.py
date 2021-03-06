class Graph:

	def __init__(self, graph_struct = None):

		if graph_struct:

			self.graph = graph_struct

		else:

			self.graph = [[0, [], 0]]

	def GetGraph(self):

		return self.graph

	def GetAllNodes(self):

		nodes = []

		for node in self.graph:

			nodes.append(node[0])

		return nodes

	def GetGraphSize(self):

		return len(self.graph)

	def GetNodeChildren(self, node_id):

		children = []

		index = -1

		for it in range(0, len(self.graph)):

			if self.graph[it][0] == node_id:

				index = it

		if index == -1:

			return "Error: Node not in Graph."

		for child in self.graph[index][1]:

			children.append(child)

		return children


	def AddNode(self):

		new_node_id = self.graph[len(self.graph)-1][0]+1

		entry = []

		entry.append(new_node_id)

		entry.append([])

		entry.append(0)

		self.graph.append(entry)

	def AddNodeWithId(self, node_id):

		entry = []

		entry.append(node_id)

		entry.append([])

		entry.append(0)

		self.graph.append(entry)

	def RemoveNode(self, node_id):

		index = -1

		for it in range(0, len(self.graph)):

			if self.graph[it][0] == node_id:

				index = it

		if index == -1:

			return "Error: Node not in Graph."

		self.graph.pop(index)


	def AddChild(self, node_id, child_id):

		nindex = cindex = -1

		for it in range(0, len(self.graph)):

			if self.graph[it][0] == node_id:

				nindex = it

			elif self.graph[it][0] == child_id:

				cindex = it

		if nindex == -1 or cindex == -1:

			return "Error: Node not in Graph."

		self.graph[nindex][1].append(child_id)

		self.graph[cindex][1].append(node_id)


	def SetNodeColor(self, node_id, color):

		for it in range(0, len(self.graph)):

			if self.graph[it][0] == node_id:

				self.graph[it][2] = color;

				break	

	def IsColored(self, node_id):

		for it in range(0, len(self.graph)):

			if self.graph[it][0] == node_id:

				if self.graph[it][2] == 1:

					return 1

				else:

					return 0

	def GetColoredNodes(self):

		colored_nodes = []

		for it in range(0, len(self.graph)):

			if self.graph[it][2] == 1:

				colored_nodes.append(self.graph[it][0])

		return colored_nodes	


					


