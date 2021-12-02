def part_1():
    hori_dist = 0
    vert_dist = 0
    with open("Day2.txt", "r") as f:
        for line in f:
            cmd = line.split()
            direction = cmd[0]
            magnitude = int(cmd[1])
            print(cmd)
            if direction == "forward":
                hori_dist += magnitude
            elif direction == "down":
                vert_dist += magnitude
            elif direction == "up":
                vert_dist -= magnitude
    print(hori_dist * vert_dist)


def part_2():
    hori_dist = 0
    vert_dist = 0
    aim = 0
    with open("Day2.txt", "r") as f:
        for line in f:
            cmd = line.split()
            direction = cmd[0]
            magnitude = int(cmd[1])
            print(cmd)
            if direction == "forward":
                hori_dist += magnitude
                vert_dist += aim * magnitude
            elif direction == "down":
                aim += magnitude
            elif direction == "up":
                aim -= magnitude
    print(hori_dist * vert_dist)


if __name__ == "__main__":
    # part_1()
    part_2()
