import numpy as np
import re

def dir(i,j):
	return -1 if i > j else 1

with open('input.txt') as f:
	input = f.readlines()

pattern = r'(\d+),(\d+) \-\> (\d+),(\d+)'

xmax, ymax = 0, 0
lines = []
for line in input:
	match = re.search(pattern, line.rstrip())
	if match:
		x1,y1,x2,y2 = match.groups()
		x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
		xmax = max(xmax, x1, x2)
		ymax = max(ymax, y1, y2)
		lines.append((x1,y1,x2,y2))

matrix = np.zeros((xmax+1,ymax+1))


def q1(): 
	for (x1,y1,x2,y2) in lines:

		if x1 != x2 and y1 != y2:
			continue
		xdir = dir(x1, x2)
		ydir = dir(y1, y2)
		for x in range(x1, x2 + xdir, xdir):
			for y in range(y1, y2 + ydir, ydir):
				matrix[x][y] += 1

	count = 0
	for index, value in np.ndenumerate(matrix):
		if value >= 2:
			count += 1

	return count

def q2(): 
	for (x1,y1,x2,y2) in lines:
		print(".")
		xdir = dir(x1, x2)
		ydir = dir(y1, y2)

		if x1 != x2 and y1 != y2:
			# assumption: these diagonals are at 45deg angles
			length = abs(x1 - x2)
			for i in range(0,length+1):
				matrix[x1 + i * xdir][y1 + i * ydir] += 1
		else:
			for x in range(x1, x2 + xdir, xdir):
				for y in range(y1, y2 + ydir, ydir):
					matrix[x][y] += 1

	count = 0
	for index, value in np.ndenumerate(matrix):
		if value >= 2:
			count += 1

	return count



# print(q1())
print(q2())