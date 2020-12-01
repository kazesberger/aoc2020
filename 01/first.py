import itertools

def get_sums(input):
    i = 0
    for a in input:
        j = i
        while j + 1 < len(input):
            j += 1
            yield a, input[j], a + input[j]


def get_matching_tuple(input):
    sums = get_sums(input)
    while True:
        try:
            matching_tuple = next(sums)
            if matching_tuple[2] == 2020:
                return matching_tuple
        except StopIteration:
            break


def get_tuples(puzzle_input, arity=2):
    index_permutations = itertools.permutations(range(0, len(puzzle_input)), arity)
    if arity == 2:
        for i, j in index_permutations:
            yield puzzle_input[i], puzzle_input[j]
    elif arity == 3:
        for i, j, k in index_permutations:
            yield puzzle_input[i], puzzle_input[j], puzzle_input[k]

def solution1(input):
    match = get_matching_tuple(input)
    return match[0] * match[1]


def solution2(input):
    matches = filter(lambda x: x[0] + x[1] == 2020,  get_tuples(input))
    first_match = next(matches)
    return first_match[0] * first_match[1]


def solve_part2(puzzle_input):
    matches = filter(lambda x: x[0] + x[1] + x[2] == 2020,  get_tuples(puzzle_input, 3))
    first_match = next(matches)
    return first_match[0] * first_match[1] * first_match[2]

# print(f'solution1: result={solution1()} time={timeit("solution1()", globals=locals(), number=100)}')
# print(f'solution2: result={solution2()} time={timeit("solution2()", globals=locals(), number=100)}')

# pprint(solution1())
# pprint(solution2())
