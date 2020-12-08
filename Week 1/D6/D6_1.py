with open('D6_in.txt') as f:
    answers = [line.strip() for line in f.readlines()]

count = 0
uniques = set()

for answer in answers:
    if answer == '':
        count += len(set(uniques))
        uniques = set()
    else:
        uniques = uniques.union(set(answer))

print(count)
