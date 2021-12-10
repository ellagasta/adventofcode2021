with open('input.txt') as f:
	lines = f.readlines()

OPEN_CHARS = ['(','[','{','<']
CLOSE_CHARS = [')',']','}','>']
OPEN_TO_CLOSE = {
	'(':')',
	'[':']',
	'{':'}',
	'<':'>'
}
CORRUPTED_CHAR_POINTS = {
	')':3,
	']':57,
	'}':1197,
	'>':25137
}
INCOMPLETE_CHAR_POINTS = {
	')':1,
	']':2,
	'}':3,
	'>':4
}

def q1(): 
	corruption_score = 0
	for line in lines:
		line = line.rstrip()

		stack = []

		for char in line:
			if char in OPEN_CHARS:
				stack.append(char)
			elif char in CLOSE_CHARS:
				if len(stack) == 0:
					corrupted = True
					break
				open_char = stack.pop()
				if OPEN_TO_CLOSE[open_char] != char:
					corruption_score += CORRUPTED_CHAR_POINTS[char]
					break
			else:
				panic("invalid char")
	print(corruption_score)

def q2():
	scores = []
	for line in lines:
		line = line.rstrip()
		stack = []

		corrupted = False
		score = 0
		for char in line:
			if char in OPEN_CHARS:
				stack.append(char)
			elif char in CLOSE_CHARS:
				if len(stack) == 0:
					corrupted = True
					break
				open_char = stack.pop()
				if OPEN_TO_CLOSE[open_char] != char:
					corrupted = True
					break
			else:
				print("invalid char")

		if not corrupted:
			stack.reverse()
			for open_char in stack:
				score = score * 5 + INCOMPLETE_CHAR_POINTS[OPEN_TO_CLOSE[open_char]]
			scores.append(score)
	scores.sort()
	print(scores[(len(scores) - 1) / 2])



q2()


