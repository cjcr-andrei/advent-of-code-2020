from collections import defaultdict

with open('D8_in.txt') as f:
    lines = [line.strip() for line in f.readlines()]

acc = 0
index = 0


def parse_line(line: str):
    split = line.split(' ')
    command = split[0]
    argument = int(split[1])

    return command, argument


def compute():
    times_visited = defaultdict(lambda: 0)
    index = 0
    acc = 0
    while index in range(len(lines)):
        times_visited[index] += 1
        if times_visited[index] >= 2:
            return acc, False
        command, argument = parse_line(lines[index])
        if command == 'acc':
            acc += argument
        elif command == 'jmp':
            index += argument
            continue
        index += 1
    return acc, True


for index in range(len(lines)):
    command, argument = parse_line(lines[index])
    old_command = f'{command} {argument}'
    if command == 'nop':
        lines[index] = f'jmp {argument}'
    elif command == 'jmp':
        lines[index] = f'nop {argument}'

    acc, flag = compute()

    if not flag:
        lines[index] = old_command
    else:
        print(acc)
        break

