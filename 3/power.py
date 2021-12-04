input = []
with open('input.txt') as f:
    input = f.readlines()
total = len(input)
wordlength = len(input[0].rstrip())
sumofpos = [0] * wordlength
for line in input:
    for pos in range(len(line.rstrip())):
        sumofpos[pos] += int(line[pos])

print(sumofpos)        

gamma = ''
epsilon = ''
for pos in range(wordlength):
    if sumofpos[pos] > total/2.0:
        gamma += '1'
        epsilon += '0'
    elif sumofpos[pos] == total/2.0:
        print("oops")
    else:
        gamma += '0'
        epsilon += '1'


print(gamma, epsilon)
print(int(gamma,2) * int(epsilon,2))
