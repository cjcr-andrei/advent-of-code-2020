from collections import defaultdict

# Create a dictionary of number frequencies, default value 0
freqs = defaultdict(lambda: 0)

# Read in all the integers from the input
with open('D1_in.txt') as f:
    numbers = [int(n) for n in f.readlines()]

for n1 in numbers:
    for n2 in numbers:
        freqs[n1] += 1
        diff = 2020 - n1 - n2

        if diff in freqs.keys():
            if n1 != n2 or (n1 == n2 and freqs[n1] >= 2):
                print(diff * n1 * n2)
                break
