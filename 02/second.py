from pprint import pprint
from timeit import timeit
import time


def get_puzzle_input(test=False):
    if test:
        with open('input-test.txt', 'r') as f:
            return f.readlines()
    else:
        with open('input.txt', 'r') as f:
            return f.readlines()


def is_valid(s: str, policy: tuple) -> bool:
    hits = filter(lambda x: x == policy[2], s)
    return policy[0] <= len(list(hits)) <= policy[1]


def is_valid_p2(s: str, policy: tuple) -> bool:
    return len(list(filter(lambda x: x == policy[2], (s[policy[0] - 1], s[policy[1] - 1])))) == 1


def parse_line(s: str):
    [lo_hi, policychar, password] = s.rsplit(' ')
    lo, hi = lo_hi.rsplit('-')
    return password, (int(lo), int(hi), policychar[0])


def solve_part1(puzzle_input):
    valid_entries = filter(lambda x: is_valid(x[0], x[1]), map(parse_line, puzzle_input))
    return len(list(valid_entries))


def solve_part2(puzzle_input):
    valid_entries = filter(lambda x: is_valid_p2(x[0], x[1]), map(parse_line, puzzle_input))
    return len(list(valid_entries))


t0 = time.process_time()
p_in = get_puzzle_input()
s1 = solve_part1(p_in)
t1 = time.process_time()
s2 = solve_part2(p_in)
t2 = time.process_time()

print(f'timeit_p1: {timeit("solve_part1(p_in)", globals=locals(), number=100)}')
print(f'timeit_p2: {timeit("solve_part2(p_in)", globals=locals(), number=100)}')

print(f's1 = {s1}, time: {t1-t0}')
print(f's2 = {s2}, time: {t2-t1}')
