import itertools

def get_tuples(puzzle_input, arity=2):
    return itertools.combinations(puzzle_input, arity)


def solve_part1(input):
    matches = filter(lambda x: x[0] + x[1] == 2020,  get_tuples(input))
    first_match = next(matches)
    return first_match[0] * first_match[1]


def solve_part2(puzzle_input):
    matches = filter(lambda x: x[0] + x[1] + x[2] == 2020,  get_tuples(puzzle_input, 3))
    first_match = next(matches)
    return first_match[0] * first_match[1] * first_match[2]
