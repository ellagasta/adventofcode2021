def main():
    input_list = []
    with open('input.txt') as f:
        input_list = f.readlines()
    
    input_list = [x.rstrip() for x in input_list]


    #input_list = ['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']
    wordlength = len(input_list[0].rstrip())
    sumofpos = [0] * wordlength
    
    oxygen = input_list[:]
    co2 = input_list[:]

    for i in range(wordlength):
        one_count = get_one_count(oxygen, i) 
        print(len(oxygen), one_count)
        if one_count >= len(oxygen)/2.0:
            oxygen = filter(lambda x: int(x[i]) == 1, oxygen)
        else: 
            oxygen = filter(lambda x: int(x[i]) == 0, oxygen)

        if len(oxygen) == 1:
            break
    
    for i in range(wordlength):
        one_count = get_one_count(co2, i) 
        if one_count >= len(co2)/2.0:
            co2 = filter(lambda x: int(x[i]) == 0, co2)
        else: 
            co2 = filter(lambda x: int(x[i]) == 1, co2)

        if len(co2) == 1:
            break
    
    print(oxygen, co2)
    print(int(oxygen[0],2) * int(co2[0], 2))

def get_one_count(input_list, pos):
    count = 0
    for line in input_list:
        count += int(line[pos])
        
    return count
main()
