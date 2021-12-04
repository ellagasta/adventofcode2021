def main():
    with open('input.txt') as f:
        lines = f.readlines()

    pos = (0, 0)
    direction_map = {
        "forward": (1,0),
        "down": (0,1),
        "up": (0,-1)
    }

    for line in lines:
        instruction = line.rstrip().split(" ")
#       print(instruction)
        delta = direction_map[instruction[0]]
        print(delta)
        pos = update_position(pos, delta, int(instruction[1]))
        print(pos)

def update_position(pos, delta, distance):
    return (pos[0]+ distance * delta[0], pos[1] + distance * delta[1])    

main()
