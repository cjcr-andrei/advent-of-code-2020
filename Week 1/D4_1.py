with open('D4_in.txt') as f:
    rows = [line.strip() for line in f.readlines()]

requirements = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
passport = set()

valid_count = 0

for row in rows:
    if row == '':
        diff = requirements - passport
        if len(diff) == 0:
            valid_count += 1
        passport = set()
    else:
        pairs = [pair for pair in row.split(' ')]
        fields = [pair.split(':')[0] for pair in pairs]
        passport = passport.union(fields)

print(valid_count)
