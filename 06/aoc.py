from pprint import pprint
import functools
import time


def get_puzzle_input(filename = 'input-test.txt'):
    with open(filename, 'r') as f:
        return map(lambda x: x.rstrip(), f.readlines())


def my_partition_anyone(it, pred):
    agg = set()
    for x in it:
        if pred(x):
            yield agg
            agg = set()
        else:
            agg.update(x)
    yield agg


def my_partition_everyone(it, pred):
    agg = set('abcdefghijklmnopqrstuvwxyz')
    for x in it:
        if pred(x):
            yield agg
            agg = set('abcdefghijklmnopqrstuvwxyz')
        else:
            agg = agg.intersection(set(x))
    yield agg


def solve_part1(puzzle_input):
    partition = list(my_partition_anyone(puzzle_input, lambda x: x == ''))
    return functools.reduce(lambda agg, x: agg + len(x), partition, 0)


def solve_part2(puzzle_input):
    partition = list(my_partition_everyone(puzzle_input, lambda x: x == ''))
    pprint(partition)
    return functools.reduce(lambda agg, x: agg + len(x), partition, 0)

# pprint(list(my_partition(get_puzzle_input(), lambda x: x == '')))


t0 = time.process_time()
s1 = solve_part1(get_puzzle_input('input.txt'))
t1 = time.process_time()
s2 = solve_part2(get_puzzle_input('input.txt'))
t2 = time.process_time()


print(f's1 = {s1}, time: {t1-t0}')
print(f's2 = {s2}, time: {t2-t1}')
