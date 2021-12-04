def main():
    with open('input.txt') as f:
        lines = f.readlines()

    pos = (0, 0, 0) # hor, dep, aim
    direction_map = {
        "down": 1,
        "up": -1
    }

    for line in lines:
        instruction = line.rstrip().split(" ")
        mag = int(instruction[1])
        if instruction[0] == "forward":
            pos = (pos[0] + mag, pos[1] + mag * pos[2], pos[2])
        else:
            delta = direction_map[instruction[0]]
            pos = (pos[0], pos[1], pos[2] + delta * mag)
        print(pos)
main()
