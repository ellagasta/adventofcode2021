import numpy as np
dots = []
instructions = []
with open('input.txt') as file:
	lines = file.readlines()

before_break = True
for line in lines:
	if line.rstrip() == "":
		before_break = False
		continue
	if before_break:
		dot = line.rstrip().split(',')
		dots.append((int(dot[0]), int(dot[1])))
	else:
		command = line.rstrip().split('fold along ')[1].split('=')
		instructions.append((command[0], int(command[1])))

def q1():
	first = instructions[0]
	# fold along x=655

	s = set()
	for x,y in dots:
		if x > 655:
			s.add((655 * 2 - x, y))
		else:
			s.add((x,y))

	print(len(s))
	

# q1()

def q2():
	s = set(dots)
	for axis, fold in instructions:
		new_s = set()
		for x, y in s:
			if axis == 'x':
				if x > fold:
					new_s.add((fold * 2 - x, y))
				else:
					new_s.add((x,y))
			elif axis == 'y':
				if y > fold:
					new_s.add((x, fold * 2 - y))
				else:
					new_s.add((x,y))
			else:
				print("AH")
		s = new_s
	x = list(s)
	x.sort()

	print(x)
q2()