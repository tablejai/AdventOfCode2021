last_record = 0
increase_count = 0

with open("Day1.txt", "r") as f:
    for line in f:
        cur_record = int(line)
        if (cur_record > last_record):
            increase_count += 1
        last_record = cur_record

print(increase_count - 1)
