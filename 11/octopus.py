import numpy as np

with open('input.txt') as f:
	lines = f.readlines()

o = []
for line in lines:
	o.append(list(line.rstrip()))

octopuses = np.array(o, dtype=int)
dim = octopuses.shape
print(dim)
flashed = np.zeros(dim)
count = 0

def neighbors(index):
	x = index[0]
	y = index[1]

	neighbors = []


	for i in range(x-1,x+2,1):
		for j in range(y-1,y+2,1):
			if not (i == x and j == y):
				if in_bounds(i) and in_bounds(j):
					neighbors.append((i, j))

	return neighbors

def in_bounds(i):
	return i >= 0 and i < dim[0]

def step():
	global flashed
	print('.')
	for index, value in np.ndenumerate(octopuses):
		octopuses[index] += 1
		if octopuses[index] > 9:
			flash(index)

	for index, value in np.ndenumerate(flashed):
		if value:
			octopuses[index] = 0
	flashed = np.zeros(dim)



def flash(index):
	global count
	if flashed[index]: # can only flash once a timestep
		return
	count += 1
	flashed[index] = True
	for neighbor in neighbors(index):
		octopuses[neighbor] += 1
		if octopuses[neighbor] > 9:
			flash(neighbor)

def q1():
	global count
	for i in range(100):
		step()
	print(count)

# q1()

def q2():
	i = 0
	while True:
		print('.')
		step()
		i += 1
		if np.all(octopuses == 0):
			break
	print(i)

q2()
