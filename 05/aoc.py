from pprint import pprint
import functools
import time

# FBFBBFF RLR
# 0101100 101
# 44      5


def get_puzzle_input(filename = 'input.txt'):
    with open(filename, 'r') as f:
        return map(lambda x: x.rstrip(), f.readlines())


def get_seat_id(seat):
    exp, row_agg = 7 + 3, 0

    for x in list(seat[:7]):
        exp -= 1
        if x == 'B':
            row_agg += int(pow(2, exp))

    exp, column_agg = 3, 0
    for x in list(seat[-3:]):
        exp -= 1
        if x == 'R':
            column_agg += int(pow(2, exp))
    return row_agg + column_agg


def solve_part1(puzzle_input):
    return max(map(lambda seat: get_seat_id(seat), puzzle_input))


def solve_part2(puzzle_input):
    last_seat = 0
    seat_ids = list(map(lambda seat: get_seat_id(seat), puzzle_input))
    seat_ids.sort()
    for s_id in seat_ids:
        if last_seat - s_id == -2:
            return s_id - 1
        else:
            last_seat = s_id


t0 = time.process_time()
s1 = solve_part1(get_puzzle_input())
t1 = time.process_time()
s2 = solve_part2(get_puzzle_input())
t2 = time.process_time()


print(f's1 = {s1}, time: {t1-t0}')
print(f's2 = {s2}, time: {t2-t1}')
