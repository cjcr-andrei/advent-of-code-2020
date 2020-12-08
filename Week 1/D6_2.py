from collections import deque

with open('D6_in.txt') as f:
    answers = [line.strip() for line in f.readlines()]

count = 0
questions = set()
queue = deque()


def get_repeated_vals(queue):
    questions = set(queue.pop())
    while len(queue) > 0:
        questions = questions.intersection(queue.pop())
    return len(questions)


for answer in answers:
    if answer == '':
        count += get_repeated_vals(queue)
    else:
        queue.append(answer)

print(count)
