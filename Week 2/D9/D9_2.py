from collections import defaultdict

with open('D9_in.txt') as f:
    lines = [int(line.strip()) for line in f.readlines()]

target = 3199139634

window_size = min(target, len(lines))

while window_size > 0:
    idx = 0
    while idx + window_size < len(lines):
        sub_array = lines[idx:idx + window_size]
        if sum(sub_array) == target:
            print(sub_array)
            print(max(sub_array) + min(sub_array))
            quit()
        idx += 1
    window_size -= 1
