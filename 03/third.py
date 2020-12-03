from pprint import pprint
import time


def get_puzzle_input(test=False) -> (int, [str]):
    filename = 'input-test.txt' if test else 'input.txt'
    with open(filename, 'r') as f:
        return len(f.readline())-1, f.readlines()


def solve_part1(puzzle_input, shift_right=3, shift_down=1):
    index_with_row = list(zip(range(1, len(puzzle_input[1]) + 1), puzzle_input[1]))
    track = [row[i * shift_right // shift_down % puzzle_input[0]] for i, row in index_with_row if i % shift_down == 0]
    # pprint(track)
    return len(list(filter(lambda x: x == '#', track)))


t0 = time.process_time()
p_in = get_puzzle_input()
s1 = solve_part1(p_in)
t1 = time.process_time()
s2 = s1 \
     * solve_part1(p_in, 1) \
     * solve_part1(p_in, 5) \
     * solve_part1(p_in, 7) \
     * solve_part1(p_in, 1, 2)
t2 = time.process_time()

print(f's1 = {s1}, time: {t1-t0}')
print(f's2 = {s2}, time: {t2-t1}')
