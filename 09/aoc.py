import time
import functools
import itertools
from pprint import pprint


def get_puzzle_input(filename='input-test.txt'):
    with open(filename, 'r') as f:
        return tuple(int(x) for x in f.readlines())


class NotValidWindowSuccessor(BaseException):
    pass


def validate_window_successor(window, successor):
    for x in window:
        if successor - x == x:
            continue
        elif successor - x in window:
            return
    raise NotValidWindowSuccessor(successor)


def solve_part1(puzzle_input, window_size=5, idx=0):
    try:
        validate_window_successor(puzzle_input[idx:idx + window_size], puzzle_input[idx + window_size])
        return solve_part1(puzzle_input, window_size, idx + 1)
    except NotValidWindowSuccessor as e:
        print(f'Validation failed on: {int(e.args[0])}')
        return int(e.args[0])


def my_reductions(f, seq, init=None):
    agg = init
    for x in seq:
        agg = f(agg, x)
        yield agg


def solve_part2(puzzle_input, first_invalid_number):
    # this could be done faster with less mem if done with 2 pointers to move the slice window - task for another day :)
    for i in range(0, len(puzzle_input) - 1):
        rest = puzzle_input[i:]
        sums = tuple(
            itertools.takewhile(lambda x: x[0] <= first_invalid_number,
                                my_reductions(lambda a, b: (a[0] + b, b), rest, (0, None))))
        # pprint(sums)
        if sums[-1][0] == first_invalid_number:
            its_a_match = tuple(x[1] for x in sums)
            # print(f'its a match! {its_a_match}')
            return min(its_a_match) + max(its_a_match)

    return 0


t0 = time.process_time()
s1 = solve_part1(get_puzzle_input('input.txt'), 25)
t1 = time.process_time()
s2 = solve_part2(get_puzzle_input('input.txt'), s1)
t2 = time.process_time()

print(f's1 = {s1}, time: {t1 - t0}')
print(f's2 = {s2}, time: {t2 - t1}')
