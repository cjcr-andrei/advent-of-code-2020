from collections import defaultdict

with open('D7_in.txt') as f:
    lines = [line.strip() for line in f.readlines()]

rules = defaultdict(lambda: [])


def memoize(func):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = func(x)
        return memo[x]
    return helper


@memoize
def bag_count(bag: str) -> int:
    bags = 1
    if not rules[bag]:
        return 1
    for entry in rules[bag]:
        bags += int(entry[0]) * bag_count(entry[1])
    return bags


for line in lines:
    key = line.split('contain')[0].strip()
    key = str.join(' ', key.split(' ')[:-1])
    contained = line.split('contain')[1].strip()
    for rule in contained.split(', '):
        number = rule[0]
        bag = str.join(' ', rule.split(' ')[1:-1])
        pair = (number, bag)
        if bag != 'other':
            rules[key].append(pair)

print(bag_count('shiny gold') - 1)
