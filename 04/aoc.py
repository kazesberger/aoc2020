from pprint import pprint
import re
import time


def my_partition(it, pred):
    agg = []
    for x in it:
        if pred(x):
            yield agg
            agg = []
        else:
            agg.extend(x.split(' '))
    yield agg


def get_puzzle_input(filename = 'input.txt') -> (int, [str]):
    with open(filename, 'r') as f:
        return [line.rstrip() for line in f.readlines() if line and len(line) > 0]


def mk_entry(scanned_document: list):
    return [(field_entry.split(':')[0], field_entry.split(':')[1]) for field_entry in scanned_document]


def parse_batch(puzzle_input):
    return map(dict, map(mk_entry, my_partition(puzzle_input, lambda x: x == '')))


def solve_part1(puzzle_input, required_fields: set):
    batch = list(parse_batch(puzzle_input))

    return len(list(filter(lambda x: required_fields.issubset(x), [document.keys() for document in batch])))


def validate_height(hgt: str):
    if hgt[-2:] not in {'cm', 'in'}:
        return False
    return 150 <= int(hgt[:-2]) <= 193 if hgt[-2:] == 'cm' else 59 <= int(hgt[:-2]) <= 76


def validate_eye_color(ecl: str):
    return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}


def validate_hair_color(hcl: str):
    return re.search('^#[a-f0-9]{6}$', hcl)


def validate_passport_id(pid: str):
    return re.search('^[0-9]{9}$', pid)


def validate_document(doc: dict):
    return 1920 <= int(doc['byr']) <= 2002 and \
           2010 <= int(doc['iyr']) <= 2020 and \
           2020 <= int(doc['eyr']) <= 2030 and \
           validate_height(doc['hgt']) and \
           validate_eye_color(doc['ecl']) and \
           validate_hair_color(doc['hcl']) and \
           validate_passport_id(doc['pid'])


def solve_part2(puzzle_input, required_fields: set):
    batch = list(parse_batch(puzzle_input))
    entries_with_req_fields = filter(lambda x: required_fields.issubset(x.keys()), batch)

    return len(list(filter(validate_document, entries_with_req_fields)))


required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

t0 = time.process_time()
p_in = get_puzzle_input()
s1 = solve_part1(p_in, required_fields)
t1 = time.process_time()
# s2 = solve_part2(get_puzzle_input('input-test-2.txt'), required_fields)
s2 = solve_part2(get_puzzle_input(), required_fields)
t2 = time.process_time()

print(f's1 = {s1}, time: {t1-t0}')
print(f's2 = {s2}, time: {t2-t1}')
