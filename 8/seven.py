with open('input.txt') as f:
	lines = f.readlines()


num_to_segment = {
	0: 6,
	1: 2,
	2: 5,
	3: 5,
	4: 4,
	5: 5,
	6: 6,
	7: 3,
	8: 7,
	9: 5
}

num_display = {
	0: set(['a','b','c','e','f','g']),
	1: set(['c','f']),
	2: set(['a','c','d','e','g']),
	3: set(['a','c','d','f','g']),
	4: set(['b','c','d','f']),
	5: set(['a','b','d','f','g']),
	6: set(['a','b','d','e','f','g']),
	7: set(['a','c','f']),
	8: set(['a','b','c','d','e','f','g']),
	9: set(['a','b','c','d','f','g'])
}

segment_signatures = { # segment: (# count, min seg length number)
	'a':(8, 3),
	'b':(6, 4),
	'c':(8, 2),
	'd':(7, 4),
	'e':(4, 5),
	'f':(9, 2),
	'g':(7, 5)
} 

segment_to_nums = {
	2: [1],
	3: [7],
	4: [4],
	5: [2,3,5,9],
	6: [0,6],
	7: [8]
}
def solve_input(input_line):
	signature_map = {
		'a':(0,10),
		'b':(0,10),
		'c':(0,10),
		'd':(0,10),
		'e':(0,10),
		'f':(0,10),
		'g':(0,10)
	}
	for input_segments in input_line:
		for segment in input_segments:
			prev_count, min_seg = signature_map[segment]
			signature_map[segment] = (prev_count + 1, min(min_seg, len(input_segments)))

	output_to_input_map = {}
	for output_segment, output_signature in signature_map.items():
		for input_segment, input_signature in segment_signatures.items():
			if output_signature == input_signature:
				output_to_input_map[output_segment] = input_segment

	return output_to_input_map

def decode_output(output_line, output_to_input_map):
	decoded_output = []
	for output in output_line: # output = 'abcd'
		input_segments = set()
		for segment in output:
			input_segments.add(output_to_input_map[segment])
		for num, segments in num_display.items():
			if input_segments == segments:
				decoded_output.append(num)
				break
	return decoded_output

def q1():
	count = 0
	for line in lines:
		split = line.rstrip().split(" ")
		input_line = split[:10]
		output_line = split[11:]

		m = solve_input(input_line)
		output_number = decode_output(output_line, m)
		num = 0
		for x in output_number:
			num = num * 10 + x
		count += num
		print(num)
	print(count)

def map_output_to_possible_inputs(output):
	possible_numbers  = segment_to_nums[len(output)]
	possible_inputs = set()
	for number in possible_numbers:
		for x in num_display[number]:
			possible_inputs.add(x)

	return possible_inputs

# print(map_output_to_possible_inputs('abcd'))
q1()
