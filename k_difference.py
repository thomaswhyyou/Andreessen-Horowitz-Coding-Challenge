import sys

first_line, second_line = sys.stdin.readlines()

n, k = [int(i) for i in first_line.split(" ")]
set_list = [int(i) for i in second_line.split(" ")]

itr_counter = 0
pair_counter = 0
while True:
    if itr_counter == n - 1:
        break

    for x in set_list[1:]:
        if abs(set_list[0] - x) == k:
            pair_counter += 1
        else:
            continue
    del set_list[0]
    itr_counter += 1

sys.stdout.write(str(pair_counter))
