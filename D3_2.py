with open('D3_in.txt') as f:
    rows = [line.strip() for line in f.readlines()]

row_length = len(rows[0])
tree = '#'


def get_tree_count(slope) -> int:
    right, down = slope
    tree_count = 0
    right_pos = 0
    for row in rows[::down]:
        if row[right_pos] == tree:
            tree_count += 1
        right_pos = (right_pos + right) % row_length

    return tree_count


inputs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
counts = list(map(get_tree_count, inputs))

product = 1
for count in counts:
    product *= count

print(product)
