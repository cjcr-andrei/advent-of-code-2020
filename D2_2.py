with open('D2_in.txt') as f:
    passwords = [(line.split(':')[0].strip(), line.split(':')[1].strip()) for line in f.readlines()]

valid_count = 0

for p in passwords:
    policy = p[0]
    password = p[1]
    range = policy.split(' ')[0]
    target_char = policy.split(' ')[1]
    pos1 = int(range.split('-')[0]) - 1
    pos2 = int(range.split('-')[1]) - 1

    if (password[pos1] == target_char or password[pos2] == target_char) \
            and (password[pos1] != password[pos2]):
        valid_count += 1

print(valid_count)
