import time


def get_puzzle_input(filename='input-test.txt'):
    with open(filename, 'r') as f:
        return map(lambda x: list(
            filter(lambda y: y not in {'bags', 'contain', 'bags.', 'bags,', 'bag,', 'bag.'}, x.rstrip().split(' '))),
                   f.readlines())


def get_bag_contents(agg_mut, contents_list):
    if len(contents_list[:3]) == 3:
        agg_mut[f'{contents_list[1]} {contents_list[2]}'] = int(contents_list[0])
        get_bag_contents(agg_mut, contents_list[3:])
    return agg_mut


def get_ancestor_bags(bag, parsed_rules):
    for k, v in parsed_rules.items():
        if v.get(bag):
            yield k
            yield from get_ancestor_bags(k, parsed_rules)


def solve_part1(puzzle_input):
    rules = list(puzzle_input)

    parsed_rules = {f'{it[0]} {it[1]}': get_bag_contents({}, it[2:]) for it in rules}

    ancestor_bags = set(get_ancestor_bags('shiny gold', parsed_rules))

    return len(ancestor_bags)


def get_contained_bags_count(bag, parsed_rules, factor=1):
    print(f'get_cont_bags_cout({bag}, rules, {factor})')
    sum = 0
    for k, v in filter(lambda x: x[0] == bag, parsed_rules.items()):
        print(f'{bag} == {k} ?')
        for child, count in v.items():
            sum += factor * count + get_contained_bags_count(child, parsed_rules, count * factor)
    return sum


def solve_part2(puzzle_input):
    rules = list(puzzle_input)

    parsed_rules = {f'{it[0]} {it[1]}': get_bag_contents({}, it[2:]) for it in rules}

    return get_contained_bags_count('shiny gold', parsed_rules)


t0 = time.process_time()
s1 = solve_part1(get_puzzle_input('input.txt'))
t1 = time.process_time()
s2 = solve_part2(get_puzzle_input('input.txt'))
t2 = time.process_time()

print(f's1 = {s1}, time: {t1 - t0}')
print(f's2 = {s2}, time: {t2 - t1}')
