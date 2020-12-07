from collections import defaultdict, deque

with open('D7_in.txt') as f:
    lines = [line.strip() for line in f.readlines()]

rules = defaultdict(lambda: [])


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper


@memoize
def contains_target_bag(bag: str) -> bool:
    for entry in rules[bag]:
        print(entry)
        if entry[1] == 'shiny gold' or contains_target_bag(entry[1]):
            return True
    return False


for line in lines:
    key = line.split('contain')[0].strip()
    key = str.join(' ', key.split(' ')[:-1])
    contained = line.split('contain')[1].strip()
    for rule in contained.split(', '):
        number = rule[0]
        bag = str.join(' ', rule.split(' ')[1:-1])
        pair = (number, bag)
        rules[key].append(pair)

count = 0
for key in rules.copy().keys():
    if contains_target_bag(key):
        count += 1

print(count)
