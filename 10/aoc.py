import time
import functools
import itertools
import collections
from pprint import pprint


def get_puzzle_input(filename='input-test.txt'):
    with open(filename, 'r') as f:
        p_in = list(int(x) for x in f.readlines())
        p_in.sort()
        return p_in


def solve_part1(puzzle_input):
    # pprint(puzzle_input)
    puzzle_input = [0] + puzzle_input + [max(puzzle_input) + 3]
    diffs = list(map(lambda x: x[0] - x[1], list(zip(puzzle_input, [0] + puzzle_input))[1:]))
    counter = collections.Counter(diffs)
    pprint(counter)
    # print(f'1: {len([x for x in diffs if x == 1])}')
    # print(f'3: {len([x for x in diffs if x == 3])}')
    return counter[1] * counter[3]


def memoize(f):
    memo = {}

    def helper(x, puzzle_input):
        if x not in memo:
            memo[x] = f(x, puzzle_input)
        return memo[x]

    return helper


@memoize
def path_count(adapter_rating, puzzle_input):
    if adapter_rating == max(puzzle_input):
        return 1
    else:
        possible_paths = list(filter(lambda x: x in puzzle_input, range(adapter_rating + 1, adapter_rating + 4)))
        # print(f'possible_paths for {adapters[0]}: {possible_paths}')
        count_recursula = []
        for next_rating in possible_paths:
            # print(state['counter'])
            # print(f'delving into path_count({adapters[i:]}, {state})')
            count_recursula.append(path_count(next_rating, puzzle_input))
        return sum(count_recursula)


def solve_part2(puzzle_input):
    pprint(puzzle_input)
    state = {'counter': 0}
    return path_count(0, puzzle_input)


t0 = time.process_time()
s1 = solve_part1(get_puzzle_input('input.txt'))
t1 = time.process_time()
s2 = solve_part2(get_puzzle_input('input.txt'))
t2 = time.process_time()

print(f's1 = {s1}, time: {t1 - t0}')
print(f's2 = {s2}, time: {t2 - t1}')
