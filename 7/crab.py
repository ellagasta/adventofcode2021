import math

with open('input.txt') as f:
	l = f.readlines()[0].rstrip()
crabs = []
for s in l.split(','):
	crabs.append(int(s))

# crabs = [16,1,2,0,4,2,7,1,2,14]

def score_single_q1(crab, pos):
	return abs(crab - pos)

def score_crabs_q1(crabs, pos):
	score = 0
	for crab in crabs:
		score += score_single_q1(crab, pos)
	return score

def q1():
	crabs.sort()
	mid = crabs[int(math.floor(len(crabs)/2))]
	mid_score = score_crabs_q1(crabs, mid)
	new = mid + 1
	new_score = score_crabs_q1(crabs, new)
	if new_score < mid_score: # optimal pos is more than mid
		while True:
			print(".")
			old = new
			old_score = new_score
			new = old + 1
			new_score = score_crabs_q1(crabs, new)
			if new_score > old_score:
				return old_score


	if new_score > mid_score: # optimal pos is less than med
		while True:
			print(".")
			old = new
			old_score = new_score
			new = old - 1
			new_score = score_crabs_q1(crabs, new)
			if new_score > old_score:
				return old_score

def score_single_q2(crab, pos):
	n = abs(crab - pos)
	return n * (n + 1) / 2

def score_crabs_q2(crabs, pos):
	score = 0
	for crab in crabs:
		score += score_single_q2(crab, pos)
	return score

def q2():
	crabs.sort()
	mid = crabs[int(math.floor(len(crabs)/2))]
	mid_score = score_crabs_q2(crabs, mid)
	new = mid + 1
	new_score = score_crabs_q2(crabs, new)

	if new_score < mid_score: # optimal pos is more than mid
		while True:
			print(".")
			old = new
			old_score = new_score
			new = old + 1
			new_score = score_crabs_q2(crabs, new)
			if new_score > old_score:
				return old_score


	if new_score > mid_score: # optimal pos is less than med
		while True:
			print(".")
			old = new
			old_score = new_score
			new = old - 1
			new_score = score_crabs_q2(crabs, new)
			if new_score > old_score:
				return old_score

print(q1())

#print(q2())

