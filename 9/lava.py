import numpy as np
with open('input.txt') as f:
	inputs = f.readlines()

m = []
for line in inputs:
	l = []
	for value in line.rstrip():
		l.append(int(value))
	m.append(l)

heightmap = np.array(m)
dim = heightmap.shape
xmax = dim[0] - 1
ymax = dim[1] - 1

low_points = []
for index, value in np.ndenumerate(heightmap):
	x = index[0]
	y = index[1]
	is_low = True

	# left
	if not x == 0:
		if heightmap[x - 1][y] <= value:
			continue
	# right
	if not x == xmax:
		if heightmap[x + 1][y] <= value:
			continue
			
	#up
	if not y == 0:
		if heightmap[x][y - 1] <= value:
			continue

	#down
	if not y == ymax:
		if heightmap[x][y + 1] <= value:
			continue
			
	if is_low:
		low_points.append(index)

def neighbors(index):
 	l = []
	x = index[0]
	y = index[1]

	if not x == 0:
		l.append(((x-1,y),heightmap[x-1,y]))
	# right
	if not x == xmax:
		l.append(((x+1,y),heightmap[x+1,y]))
			
	#up
	if not y == 0:
		l.append(((x,y-1),heightmap[x,y-1]))

	#down
	if not y == ymax:
		l.append(((x,y+1),heightmap[x,y+1]))

	return l

def q1():
	sum_risk = 0
	for low_point in low_points:
		sum_risk += 1 + heightmap[low_point]

	print(sum_risk)

# q1()

def q2():
	basin_sizes = []
	count = 0
	for low_point in low_points:
		basin_size = dfs(low_point)
		basin_sizes.append(basin_size)
		count += basin_size
	basin_sizes.sort()
	print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])

def dfs(low_point):
	q = [low_point]
	size = 0
	while len(q) != 0:
		to = q.pop(0)
		to_val = heightmap[to[0]][to[1]]
		if to_val == 9: #already counted
			continue
		size += 1
		for neighbor, neighbor_value in neighbors(to):
			if neighbor_value > to_val and neighbor_value != 9:
				q.append(neighbor)
		heightmap[to[0]][to[1]] = 9
	return size

q2()

