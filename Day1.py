def part_1():
    last_record = 0
    increase_count = 0

    with open("Day1.txt", "r") as f:
        for line in f:
            cur_record = int(line)
            if (cur_record > last_record):
                increase_count += 1
            last_record = cur_record

    print(increase_count - 1)


def part_2():
    window = []
    last_sum = 0
    increase_count = 0

    with open("Day1.txt", "r") as f:
        for line in f:
            window.append(int(line))
            print(window)
            if len(window) == 3:
                window_sum = window[0] + window[1] + window[2]
                if (window_sum > last_sum):
                    increase_count += 1
                last_sum = window_sum
                window.pop(0)

    print(increase_count - 1)


if __name__ == '__main__':
    # part_1()
    part_2()
