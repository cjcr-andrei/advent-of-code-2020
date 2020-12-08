with open('D3_in.txt') as f:
    rows = [line.strip() for line in f.readlines()]

row_length = len(rows[0])
tree = '#'
tree_count = 0
right_pos = 0

for row in rows:
    if row[right_pos] == tree:
        tree_count += 1
    right_pos = (right_pos + 3) % row_length

print(tree_count)
