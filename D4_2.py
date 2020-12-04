import re

with open('D4_in.txt') as f:
    rows = [line.strip() for line in f.readlines()]

requirements = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
passport_fields = []
passport_data = []

hcl_pattern = r'([a-f]|[0-9])+'
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

valid_count = 0


def check_data_validity(passport: dict) -> bool:
    byr = passport['byr']
    if not (byr.isdigit() and len(byr) == 4 and 1920 <= int(byr) <= 2002):
        return False

    iyr = passport['iyr']
    if not (iyr.isdigit() and len(iyr) == 4 and 2010 <= int(iyr) <= 2020):
        return False

    eyr = passport['eyr']
    if not (eyr.isdigit() and len(eyr) == 4 and 2020 <= int(eyr) <= 2030):
        return False

    hgt = passport['hgt']
    if 'cm' not in hgt and 'in' not in hgt:
        return False

    unit = hgt[-2:]
    height = int(hgt[:-2])
    if (unit == 'cm' and not 150 <= height <= 193) or (unit == 'in' and not 59 <= height <= 76):
        return False

    hcl = passport['hcl']
    code = hcl[1:]
    if hcl[0] != '#' or len(code) != 6 or not re.match(hcl_pattern, code):
        return False

    if passport['ecl'] not in eye_colors:
        return False

    if len(passport['pid']) != 9 or not passport['pid'].isdigit():
        return False

    return True


for row in rows:
    if row == '':
        passport = dict(zip(passport_fields, passport_data))
        diff = requirements - set(list(passport.keys()))

        if len(diff) == 0 and check_data_validity(passport):
            valid_count += 1

        passport_fields = []
        passport_data = []

    else:
        pairs = [pair for pair in row.split(' ')]
        passport_fields.extend([pair.split(':')[0] for pair in pairs])
        passport_data.extend([pair.split(':')[1] for pair in pairs])

print(valid_count)
