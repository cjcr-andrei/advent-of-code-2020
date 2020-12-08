from collections import defaultdict

# Create a dictionary of number frequencies, default value 0
freqs = defaultdict(lambda: 0)

# Read in all the integers from the input
with open('D1_in.txt') as f:
    numbers = [int(n) for n in f.readlines()]

for n in numbers:
    freqs[n] += 1
    diff = 2020 - n

    # Counterpart of the number n occurs at least once? Multiply them and stop here
    if diff in freqs.keys():
        print(diff * n)
        break
