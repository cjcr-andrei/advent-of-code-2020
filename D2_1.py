with open('D2_in.txt') as f:
    passwords = [(line.split(':')[0].strip(), line.split(':')[1].strip()) for line in f.readlines()]

valid_count = 0

for p in passwords:
    policy = p[0]
    password = p[1]
    limits = policy.split(' ')[0]
    target_char = policy.split(' ')[1]
    lower_limit = int(limits.split('-')[0])
    upper_limit = int(limits.split('-')[1])
    target_count = 0
    for c in password:
        if c == target_char:
            target_count += 1

    if lower_limit <= target_count <= upper_limit:
        valid_count += 1

print(valid_count)
