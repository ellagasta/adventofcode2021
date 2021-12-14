with open('input.txt') as f:
	lines = f.readlines()

nodes = set()
smalls = set()
m = {}

for line in lines:
	nodeA, nodeB = line.rstrip().split('-')
	if nodeA.islower():
		smalls.add(nodeA)
	if nodeB.islower():
		smalls.add(nodeB)

	nodes.add(nodeA)
	nodes.add(nodeB)

	if nodeA in m.keys():
		m[nodeA].add(nodeB)
	else:
		m[nodeA] = set([nodeB])

	if nodeB in m.keys():
		m[nodeB].add(nodeA)
	else:
		m[nodeB] = set([nodeA])

# print(nodes)
# print(smalls)
# print(m)

# def q1():

# 	def find_path(path, node, visited_smalls):
# 		path.append(node)
# 		if node == 'end':
# 			global paths
# 			paths.append(path)

# 		if node in smalls:
# 			visited_smalls.add(node)

# 		for neighbor in m[node]:
# 			if neighbor not in visited_smalls:
# 				new_path = path[:]
# 				new_visited_smalls = visited_smalls.copy()
# 				find_path(new_path, neighbor, new_visited_smalls)



# 	paths = []

# 	visited_smalls = set()

# 	find_path([], 'start', visited_smalls)

# 	print(len(paths))

# q1()

def q2():
	paths = []
	def find_path(path, node, visited_smalls, twice_visited):
		path.append(node)
		if node == 'end':
			paths.append(path)
			return

		if node in smalls:
			if node in visited_smalls:
				twice_visited = True
			else:
				visited_smalls.add(node)

		for neighbor in m[node]:
			if neighbor != 'start':

				if (neighbor not in visited_smalls) or not twice_visited:
					new_path = path[:]
					new_visited_smalls = visited_smalls.copy()
					find_path(new_path, neighbor, new_visited_smalls, twice_visited)




	visited_smalls = set()

	find_path([], 'start', visited_smalls, False)

	print(len(paths))
q2()