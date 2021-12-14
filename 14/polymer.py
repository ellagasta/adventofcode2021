from collections import defaultdict

def q1():
	with open('input.txt') as f:
		l = f.readlines()

	polymer = l.pop(0).rstrip() # initial polymer
	l.pop(0) # empty line
	rules = {}
	for line in l: # rules
		parsed = line.rstrip().split(' -> ')
		pattern, insertion = parsed[0], parsed[1]
		rules[pattern] = insertion

	for n in range(10):
		insert_after = {}
		for i in range(len(polymer) - 1):
			frame = polymer[i:i+2]
			print(frame)
			if frame in rules.keys():
				insert_after[i] = rules[frame]

		new_polymer = ''
		for i in range(len(polymer)):
			new_polymer += polymer[i]
			if i in insert_after.keys():
				new_polymer += insert_after[i]
		polymer = new_polymer

	char_count = {}
	for char in polymer:
		if char in char_count.keys():
			char_count[char] += 1
		else:
			char_count[char] = 1
	print(char_count)

# q1()

def q2():
	with open('input.txt') as f:
		l = f.readlines()

	polymer = l.pop(0).rstrip() # initial polymer
	l.pop(0) # empty line
	rules = {}
	for line in l: # rules
		parsed = line.rstrip().split(' -> ')
		pattern, insertion = parsed[0], parsed[1]
		p1, p2 = pattern[0], pattern[1]

		rules[pattern] = [p1+insertion, insertion+p2]

	frame_count = defaultdict(lambda: 0)

	for i in range(len(polymer) - 1):
		frame = polymer[i:i+2]
		frame_count[frame] += 1

	for i in range(40):
		print(i)
		new_frame_count = defaultdict(lambda: 0)
		for key, num in frame_count.items():
			e1, e2 = rules[key]
			new_frame_count[e1] += num
			new_frame_count[e2] += num
		frame_count = new_frame_count

	char_count = defaultdict(lambda:0)	
	for key, num in frame_count.items():
		char_count[key[0]] += num
		char_count[key[1]] += num

	# first and last char of input is singlely counted, rest is double counted. doubley count all
	char_count[polymer[0]] += 1
	char_count[polymer[-1]] += 1

	print(char_count)
	maxi, mini = max(char_count.values())/2, min(char_count.values())/2
	print(maxi, mini, maxi-mini)
q2()
