from collections import defaultdict

with open('D9_in.txt') as f:
    lines = [int(line.strip()) for line in f.readlines()]


def two_sum(arr: list, sum: int, freqs: dict) -> bool:
    for key in arr:
        diff = sum - key
        if (diff != key and freqs[diff] > 0) or (diff == key and freqs[diff] >= 2):
            return True
    return False


freqs = defaultdict(lambda: 0)

preamble_length = 25

prev_key = ''

for index in range(preamble_length):
    freqs[lines[index]] += 1

for index in range(preamble_length, len(lines)):
    prev_key = lines[index - preamble_length]
    preamble = lines[index - preamble_length:index]

    if not two_sum(preamble, lines[index], freqs):
        print(lines[index])
        break
    freqs[lines[index]] += 1
    freqs[prev_key] -= 1
