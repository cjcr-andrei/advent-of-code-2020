import math

with open('D5_in.txt') as f:
    boarding_passes = [line.strip() for line in f.readlines()]


def get_seat_id(boarding_pass: str) -> int:
    rows = [i for i in range(128)]
    row_lower_bound = 0
    row_upper_bound = len(rows)
    row_indicator = boarding_pass[:-3]

    cols = [i for i in range(8)]
    col_lower_bound = 0
    col_upper_bound = len(cols)
    col_indicator = boarding_pass[-3:]

    for half in row_indicator:
        row_lower_bound, row_upper_bound = update_bounds(half, row_lower_bound, row_upper_bound)

    row = min(row_lower_bound, row_upper_bound)

    for half in col_indicator:
        col_lower_bound, col_upper_bound = update_bounds(half, col_lower_bound, col_upper_bound)

    col = min(col_lower_bound, col_upper_bound)

    return row * 8 + col


def update_bounds(half, lower_bound, upper_bound):
    if half == 'F' or half == 'L':
        upper_bound = math.floor((upper_bound + lower_bound) / 2)
    else:
        lower_bound = math.ceil((upper_bound + lower_bound) / 2)
    return lower_bound, upper_bound


seat_id = max(map(get_seat_id, boarding_passes))
print(seat_id)
